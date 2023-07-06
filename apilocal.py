from flask import Flask, request, jsonify
import mysql.connector
import os

app = Flask(__name__)

mysql_host = os.environ.get('MYSQL_HOST', '127.0.0.1')
mysql_password = os.environ.get('MYSQL_PASSWORD', 'safouene')
mysql_user = os.environ.get('MYSQL_USER', 'root')


def get_connection():
    return mysql.connector.connect(
        user=mysql_user, password=mysql_password, host=mysql_host, port=3306, database='user'
    )


@app.route('/xxx/v<int:version>', methods=['GET'])
def get_versions(version):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM tab')
    version_users = cursor.fetchall()
    connection.close()
    return jsonify({"version": version, "data": version_users})


@app.route('/xxx/v<int:version>', methods=['POST'])
def post_user(version):
    data = request.json
    connection = get_connection()
    cursor = connection.cursor()
    insert = 'INSERT INTO tab (id, name, lastname, version_id) VALUES (%s, %s, %s, %s)'
    values = (data["id"], data["name"], data["lastname"], version)
    cursor.execute(insert, values)
    connection.commit()
    connection.close()
    return {"version": version, "message": "User created"}


@app.route('/xxx/v<int:version>/<int:user_id>', methods=['GET'])
def get_user(version, user_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM tab WHERE id = %s AND version_id = %s', (user_id, version))
    user = cursor.fetchone()
    connection.close()
    if user:
        response = {
            "version": version,
            "user": {
                "id": user[0],
                "name": user[1],
                "lastname": user[2]
            }
        }
        return response
    return jsonify({"version": version, "message": "User not found"})


@app.route('/xxx/v<int:version>/<int:user_id>', methods=['PUT'])
def put_user(version, user_id):
    data = request.json
    connection = get_connection()
    cursor = connection.cursor()
    update = 'UPDATE tab SET name = %s, lastname = %s WHERE id = %s AND version_id = %s'
    values = (data["name"], data["lastname"], user_id, version)
    cursor.execute(update, values)
    connection.commit()
    connection.close()
    return {"version": version, "message": "User updated"}


@app.route('/xxx/v<int:version>/<int:user_id>', methods=['DELETE'])
def delete_user(version, user_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('DELETE FROM tab WHERE id = %s AND version_id = %s', (user_id, version))
    connection.commit()
    connection.close()
    return {"version": version, "message": "User deleted"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)







    



