import sqlite3 as db

conn = db.connect('dbex1.db')

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS daylyreciept
          (
          pay integer ,
          wf text
          )
          """)

def ins_reciept (nureciept):
    with conn:
        c.execute('INSERT INTO daylyreciept VALUES (:pay , :wf)',{'pay' :nureciept.pay , 'wf' :nureciept.wf})
        
def reciept_getter():
    with conn:
        c.execute('SELECT * FROM daylyreciept')
        
def get_reciept_byWF(watf):
    with conn:
        c.execute('SELECT * FROM daylyreciept WHERE wf = :wf' , {'wf': watf})
        return c.fetchall()
        
        
    
    