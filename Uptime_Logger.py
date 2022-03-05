import datetime
import random
from time import sleep

from pythonping import ping

ping_count = 0
while ping_count >= 0:
    sleep_duration = random.randint(1800, 3600)
    sleep_duration_pretty = f'{round(sleep_duration / 60)} minutes {sleep_duration % 60} seconds'
    print(sleep_duration_pretty)
    check_ping = ping('1.1.1.1', verbose=True)
    uptime_log = open('uptime_check_log.txt', 'a')
    time_stamp = datetime.datetime.now()
    print(time_stamp)
    tildes = '~' * 80
    ping_count += 1
    uptime_log.writelines(
        f'{tildes}{ping_count}\nAs of {time_stamp}:\n{str(check_ping)} \nsleep time: {sleep_duration} seconds, or {sleep_duration_pretty}\n')
    sleep(sleep_duration)
