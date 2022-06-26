# задача простая, но что-то я в ней подзапуталась

n = int(input())
arr = sorted(set(map(int, input().split())))
answer = ""
n = len(arr)
i = 1
begin, end = 0, 0

while i < n:

    while i < n and arr[i] == arr[i-1] + 1:
        i += 1
        end += 1

    long = ', '.join(map(str, arr[begin:end+1]))
    short = str(arr[begin]) + ', ..., ' + str(arr[end])
    if len(long) < len(short):
        answer = answer + ', ' + long if len(answer) > 0 else long
    else:
        answer = answer + ', ' + short if len(answer) > 0 else short
    begin, end = i, i
    i += 1

if end < n:
    long = ', '.join(map(str, arr[begin:end+1]))
    short = str(arr[begin]) + ', ..., ' + str(arr[end])
    if len(long) < len(short):
        answer = answer + ', ' + long if len(answer) > 0 else long
    else:
        answer = answer + ', ' + short if len(answer) > 0 else short

print(answer)
