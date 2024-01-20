from docopt import docopt
from api import *
import tabulate

Usage = ''' 
             Usage : 
                 spent_app.py --init
                 spent_app.py --show [<category>]
                 spent_app.py --add <amount> <category> [<message>]
        '''

val = docopt(Usage)

if val['--init']:
    init()
    print('Your table successfully created.. ')

if val['--show']:
    category = val['<category>']
    amount, results = show(category)
    results = [list(x) for x in results.fetchall()]
    print('Total expense: ', amount)
    print(tabulate.tabulate(results))

if val['--add']:
    try:
        amount = float(val['<amount>'])
        message = str(val['<message>']) if val['<message>'] else ''
        add(amount, val['<category>'], message)
        print('Item added')
    except:
        print(Usage)
        
    conn.close()