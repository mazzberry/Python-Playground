

import webbrowser
import random
import time


while True:
    sites = random.choice(['', '', ''])

    webbrowser.open(sites)

    seconds = random.randrange(5, 20)
    time.sleep(seconds)
