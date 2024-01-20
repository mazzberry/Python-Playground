# fuci baray : inset , select All , ger

import sqlite3 as db
from orgkarmand import karmand
from tabulate import tabulate


conn = db.connect('myDb3.db')


c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS karmand
          
          (
    
    
    name text,
    
    lname text,
    
    salary integer
    
    
         )
          
          ''')


def insert_emp(emp):
    # bejay neveshtan commit az : with conn : estefade mikonim
    with conn:
        c.execute('INSERT INTO karmand VALUES (:name, :lname, :salary)', {
                  'name': emp.name, 'lname': emp.lname, 'salary': emp.salary})


def getEmpByLname(lastname):
    c.execute('SELECT * FROM karmand WHERE lname = :lname',
              {'lname': lastname})
    return c.fetchall()


def getAllEmp():
    c.execute('SELECT * FROM karmand')
    return c.fetchall()


def updateSalary(emp, salary):
    with conn:
        c.execute(""" UPDATE karmand SET salary = :salary
                    WHERE name = :name AND lname = :lname  """,
                  {'name': emp.name, 'lname': emp.lname, 'salary': emp.salary})


def removeEmp(emp):
    with conn:
        c.execute(""" DELETE from karmand WHERE name = :name AND lname = :lname """,
                  {'name': emp.name, 'lname': emp.lname})


emp_1 = karmand('ali', 'mohammadi', 3000)
emp_2 = karmand('alireza', 'akbarnejad', 4500)
emp_3 = karmand('naser', 'kadeie', 5000)
emp_4 = karmand('sara', 'eskandary', 3200)
emp_5 = karmand('yasin', 'eghbal', 4500)
emp_6 = karmand('reza', 'parinia', 6000)

# insert_emp(emp_1)
# insert_emp(emp_2)
# insert_emp(emp_3)
# insert_emp(emp_4)
# insert_emp(emp_5)
# insert_emp(emp_6)

# removeEmp(emp_3)
emps = getAllEmp()

updateSalary(emp_2, 1000)

# emps = getEmpByLname('eskandary')

# emps = getEmpByLnameALL('eghbal')
# emps = getAllEmp()
print(tabulate(emps))

conn.close()
