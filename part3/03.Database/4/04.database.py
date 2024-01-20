import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost' , 
    user = 'root' , 
    password = 'Mzh16/10/82__Om'
)

# baray test :print(mydb)

c= mydb.cursor()

#c.execute ('CREATE DATABASE testmydb')
c.execute ('SHOW DATABASES')


for db in c:
    print(db)



