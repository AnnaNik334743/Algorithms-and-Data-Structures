from datetime import datetime


trains = {}
for _ in range(int(input())):
    line = input()
    _, name, times = line.split('"')
    secs = (datetime.strptime(times.split()[1], "%H:%M") - datetime.strptime(times.split()[0], "%H:%M")).seconds
    trains[name] = secs if secs != 0 else 86400
name, secs = min(trains.items(), key=lambda para: para[1])
print(f'The fastest train is "{name}".')
print(f'Its speed is {round(650 * 60 * 60 / secs)} km/h, approximately.')
