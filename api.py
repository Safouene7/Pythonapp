from time import sleep
from flask import Flask, request, jsonify
import mysql.connector
import os
import socket

app = Flask(__name__)

mysql_host = os.environ.get('MYSQL_HOST', 'mysql')
mysql_password = os.environ.get('MYSQL_PASSWORD', 'password')
mysql_user = os.environ.get('MYSQL_USER', 'root')


def get_connection():
    return mysql.connector.connect(
        user=mysql_user, password=mysql_password, host=mysql_host, port=3306, database='user'
    )

from flask import Response

@app.route('/info', methods=['GET'])
def get_info_hostname():
    sleep(10)
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    
    response_content = f"Hostname: {hostname}\nIP Address: {ip_address}"
    response = Response(response_content, status=200, headers={'Custom-Header': 'Custom Value'})
    
    return response




@app.route('/xxx', methods=['GET'])
def get_users():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM tab')
    users = cursor.fetchall()
    connection.close()
    return jsonify({"data": users})


@app.route('/xxx', methods=['POST'])
def post_user():
    data = request.json
    connection = get_connection()
    cursor = connection.cursor()
    insert = 'INSERT INTO tab (id, name, lastname) VALUES (%s, %s, %s)'
    values = (data["id"], data["name"], data["lastname"])
    cursor.execute(insert, values)
    connection.commit()
    connection.close()
    return {"message": "User created"}


@app.route('/xxx/<int:user_id>', methods=['GET'])
def get_user(user_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM tab WHERE id = %s', user_id)
    user = cursor.fetchone()
    connection.close()
    if user:
        response = {
            "user": {
                "id": user[0],
                "name": user[1],
                "lastname": user[2]
            }
        }
        return response
    return jsonify({"message": "User not found"})


@app.route('/xxx/<int:user_id>', methods=['PUT'])
def put_user(user_id):
    data = request.json
    connection = get_connection()
    cursor = connection.cursor()
    update = 'UPDATE tab SET name = %s, lastname = %s'
    values = (data["name"], data["lastname"], user_id)
    cursor.execute(update, values)
    connection.commit()
    connection.close()
    return {"message": "User updated"}


@app.route('/xxx/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('DELETE FROM tab WHERE id = %s', user_id)
    connection.commit()
    connection.close()
    return {"message": "User deleted"}

if __name__ == '__main__':
    app.run(host='0.0.0.0',threaded=True)







    



