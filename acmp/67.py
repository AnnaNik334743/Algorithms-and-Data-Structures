masks = []
for _ in range(int(input())):
    masks.append(list(map(int, input().split('.'))))
for _ in range(int(input())):
    pair1, pair2 = map(lambda item: list(map(int, item.split('.'))), input().split())
    counter = 0
    for mask in masks:
        if ((mask[0] & pair1[0] == mask[0] & pair2[0]) and
            (mask[1] & pair1[1] == mask[1] & pair2[1]) and
            (mask[2] & pair1[2] == mask[2] & pair2[2]) and
            (mask[3] & pair1[3] == mask[3] & pair2[3])):
            counter += 1
    print(counter)
