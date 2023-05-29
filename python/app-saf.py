import mysql.connector

connection = mysql.connector.connect(
    user='root', password='safouene', host='mysql', port="3306", database='student')
print("DB connected")

cursor = connection.cursor()
cursor.execute('Select * FROM student.students')
students = cursor.fetchall()
connection.close()

print(students)
