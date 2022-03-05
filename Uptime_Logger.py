import datetime
import random
from time import sleep

from pythonping import ping

while True:
    sleep_duration = random.randint(1800, 3600)
    sleep_duration_pretty = f'{round(sleep_duration / 60)} minutes {sleep_duration % 60} seconds'
    print(sleep_duration_pretty)
    check_ping = ping('1.1.1.1', verbose=True)
    uptime_log = open('uptime_check_log.txt', 'a')
    time_stamp = datetime.datetime.now()
    print(time_stamp)
    uptime_log.writelines((str(check_ping) + f'\nsleep time: {sleep_duration} seconds, or {sleep_duration_pretty}\n\n'))
    sleep(sleep_duration)
