import mysql.connector

mydb = mysql.connector.connect(
 host = 'localhost',
 user = 'tops',
 password = 'murari',
 database = 'guiproject'
 
)

c1 = mydb.cursor()
c1.execute('CREATE TABLE customers (name VARCHAR(255), email VARCHAR(255), number INT(255), city VARCHAR(255), gender BOOL)')
