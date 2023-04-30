input()
mx = 0
buses_dict = {}
buses = list(map(int, input().split()))
for i, bus in enumerate(buses):
    try:
        prev_bus_i = buses_dict[bus]
        if i - prev_bus_i > mx:
            mx = i - prev_bus_i
    except KeyError:
        pass
    buses_dict[bus] = i
print(mx)
