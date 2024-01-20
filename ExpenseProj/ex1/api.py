import sqlite3 as db
from datetime import datetime

conn = db.connect('dbex1.db')

c = conn.cursor()


def init():
    with conn:
        c.execute("""CREATE TABLE IF NOT EXISTS expenses
                (
                 amount REAL ,
                category TEXT COLLATE NOCASE,
                message TEXT,
                date TEXT
             )
             """)


def add(amount, category, message=''):
    # adds new items to db

    date = str(datetime.now().strftime(r'%Y - %m - %d | %H:%M'))

    c.execute("INSERT INTO expenses VALUES (:amount , :message , :category , :date)",
              {'amount': amount, 'message': message, 'category': category, 'date': date})
    conn.commit()


def show(category=None):
    # showing all data in db
    if category:
        c.execute('SELECT * FROM expenses WHERE category = (:category)',
                  {'category': category})
        results = c.fetchall()
        c.execute('SELECT sum(amount) FROM expenses WHERE category = (:category)', {
                  'category': category})
        totalamount = c.fetchone()[0]
        
        return totalamount , results

    else:

        c.execute('SELECT * FROM expenses')
        results = c.fetchall()
        c.execute('SELECT sum(amount) FROM expenses')
        totalamount = c.fetchone()[0]

    return totalamount, results


# init()

# add(900, 'food')
# add(800, 'snap')
# add(1000, 'adams')
print(show('snap'))
