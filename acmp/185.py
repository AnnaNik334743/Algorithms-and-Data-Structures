def main():
    n, k = map(int, input().split())
    horses = {i: {"upper": None, "lower": None} for i in range(1, n + 1)}
    while (s := input()) != '0':
        faster, slower = map(int, s.split())
        horses[faster]["lower"] = slower
        horses[slower]["upper"] = faster
    for val, bounds in horses.items():
        if val != k and bounds["upper"] is None:
            return 'No'
    return 'Yes'


print(main())