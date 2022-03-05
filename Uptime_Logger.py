import datetime
import random
from time import sleep

from pythonping import ping

while True:
    x = random.randint(1800, 3600)
    print(x / 60)
    y = ping('1.1.1.1', verbose=True)
    uptime_log = open('uptime_check_log.txt', 'a')
    time_stamp = datetime.datetime.now()
    print(time_stamp)
    uptime_log.writelines((str(y) + f'\nsleep time: {x} seconds.\n\n'))
    sleep(x)
