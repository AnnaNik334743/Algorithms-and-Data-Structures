a = sorted(filter(lambda x: ~x % 2 and x // 64 % 2, map(int, list(open(0))[1].split())))
p = print
p(len(a))
p(*a)
