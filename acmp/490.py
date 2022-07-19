import datetime


def c(s):
    return datetime.datetime.strptime(s, '%d.%m.%y').date()


i = input
print(abs(c(i()) - c(i())).days)
