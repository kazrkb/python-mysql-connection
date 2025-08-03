import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', passwd = '1234', database='sakila')

mycursor = mydb.cursor()
mycursor.execute('SELECT * FROM actor')
result = mycursor.fetchall()

for i in result:
    print(i)