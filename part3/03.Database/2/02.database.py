import sqlite3 as db
from orgkarmand import karmand


conn = db.connect('karmand_db2.db')


c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS karmand
          
          (
    
    
    name text,
    
    lname text,
    
    salary integer
    
    
         )
          
          ''')


emp_1 = karmand('Mohammadreza', 'Hosseini', 32000)
emp_2 = karmand('Mina', 'Mohebi', 34000)

#dar in noe az vared kardan etelaat : mored hamle sqlinjection qarar migirim pas az ravesh digari mirim
##c.execute('INSERT INTO karmand VALUES ("{}" , "{}" , {})'.format(emp_1.name , emp_1.lname , emp_1.salary))
##conn.commit()

#dar in ravesh dar ()bad VALUE betedad anasor vorudi (:) qarar midim ke be surat zir hast:
##c.execute('INSERT INTO karmand VALUES (:name, :lname, :salary)', {'name': emp_1.name , 'lname': emp_1.lname , 'salary': emp_1.salary})
##conn.commit()
 
##c.execute('INSERT INTO karmand VALUES (:name, :lname, :salary)', {'name': emp_2.name , 'lname': emp_2.lname , 'salary': emp_2.salary})
##conn.commit()

##c.execute('SELECT * FROM karmand')

#az fetchall mitoonim tory estefade konim ke moredi az db bekeshe biroon masalan : harchi hosseini hast ro namayesh bede
c.execute('SELECT * FROM karmand WHERE lname = :lname', {'lname' : 'Hosseini'})


print(c.fetchall())

#for a in c.fetchall():
   # print(a, end='\n')


conn.close() 