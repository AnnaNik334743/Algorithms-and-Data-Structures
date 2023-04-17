my_counter = {}
l = list(map(int, input().split()))
for num in l:
    try:
        my_counter[num] += 1
    except KeyError:
        my_counter[num] = 1
vals = my_counter.values()
if 5 in vals:
    print("Impossible")
elif 4 in vals:
    print("Four of a Kind")
elif 2 in vals and 3 in vals:
    print("Full House")
elif sorted(l) == list(range(min(l), max(l) + 1)):
    print("Straight")
elif 3 in vals:
    print("Three of a Kind")
elif list(vals).count(2) == 2:
    print("Two Pairs")
elif 2 in vals:
    print("One Pair")
else:
    print("Nothing")

