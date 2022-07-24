def prefix_function(s):
    p = [0] * (len(s) + 1)
    i, j = 1, 0
    while i < len(s):
        if s[i] == s[j]:
            p[i + 1] = j + 1
            i += 1
            j += 1
        else:
            if j > 0:
                j = p[j]
            else:
                p[i + 1] = 0
                i += 1
    return p[1::]


init_string = input()
dp = [float('inf') for _ in init_string + ' ']
dp[-1] = 0
dp_index = [None for _ in init_string]

for begin in range(len(init_string)):
    pref = prefix_function(init_string[begin:])

    for len_of_curr_str, num_from_pref in enumerate(pref):
        len_of_curr_str += 1  # it has to be length, not just index
        cycle_length = len_of_curr_str - num_from_pref
        end = (len_of_curr_str // cycle_length) * cycle_length + begin - 1

        option1 = dp[begin - 1] + cycle_length
        option2 = dp[end - 1] + 1
        if option1 < dp[end]:
            dp[end] = option1
            dp_index[end] = begin - 1
        if option2 < dp[end]:
            dp[end] = option2
            dp_index[end] = end - 1

dp = dp[:-1]
print(dp[-1])

path = []
to_here = len(init_string) - 1
while dp_index[to_here] != -1:
    we_come_from = dp_index[to_here]
    len_cycle = dp[to_here] - dp[we_come_from]
    inner_string = init_string[we_come_from + 1: to_here + 1]
    inner_string, multiple = inner_string[:len_cycle], (to_here - we_come_from) // len_cycle
    to_here = we_come_from
    if multiple == 1 and len(path) > 0 and path[-1][1] == 1:
        path[-1][0] = inner_string + path[-1][0]
    else:
        path.append([inner_string, multiple])
else:
    we_come_from = 0
    len_cycle = dp[to_here]
    inner_string = init_string[:to_here + 1]
    inner_string, multiple = inner_string[:len_cycle], (to_here + 1) // len_cycle
    if multiple == 1 and len(path) > 0 and path[-1][1] == 1:
        path[-1][0] = inner_string + path[-1][0]
    else:
        path.append([inner_string, multiple])

for item in path[::-1]:
    print(*item)