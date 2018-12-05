#!/bin/env python3
import datetime


def to_timestamp(date, time):
    ts = datetime.datetime.strptime(date + " " + time, "[%Y-%m-%d %H:%M]")
    return(ts)


logs = []
with open("day04_input.txt", "r") as f:
    for line in f:
        date, time, *log = line.strip().split(" ")
        timestamp = to_timestamp(date, time)
        tmp_dic = {'timestamp': timestamp, 'log': log}
        logs.append(tmp_dic)
logs = sorted(logs, key=lambda x: x['timestamp'])
for log in logs:
    if 'Guard' in log['log']:
        log['status'] = 'start'
    elif 'falls' in log['log']:
        log['status'] = 'sleep'
    elif 'wakes' in log['log']:
        log['status'] = 'up'
    else:
        log['status'] = 'unknown'
# print(logs)
# nop = [log for log in logs if log['status'] == 'up']
# print(nop)
ids = [log['log'][1] for log in logs if log['status'] == 'start']
print(ids)
