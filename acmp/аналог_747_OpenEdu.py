# пока это максимально оптимальный код, который доходит до 37 теста на OpenEdu
# нужно переписывать на плюсы, иначе ему не поможешь

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


init_string = ' ' + open('input.txt', 'r').readline().strip()  # indexing from 1

dp = [float('inf') for _ in init_string]
dp[0] = 0
dp_directions = [-1 for _ in init_string]
dp_directions[0] = float('inf')
dp_labels = ['n' for _ in init_string]  # 'n' for not_cycle, 'c' for cycle
dp_length_cycles = [1 for _ in init_string]

for begin in range(1, len(init_string) + 1):
    pref = prefix_function(init_string[begin:])

    for len_of_curr_str, num_from_pref in enumerate(pref):

        len_of_curr_str += 1  # it has to be length, not just index
        cycle_length = len_of_curr_str - num_from_pref
        num_of_repetitions = len_of_curr_str // cycle_length
        end = (len_of_curr_str // cycle_length) * cycle_length + begin - 1

        if num_of_repetitions == 1:
            # its just a symbol, not a cycle
            option = dp[end - 1]
            option += 1 if dp_labels[end - 1] == 'n' else 2  # if it is a cycle, we add +
            if option <= dp[end]:
                dp[end] = option
                dp_directions[end] = end - 1
                dp_labels[end] = 'n'
        else:
            # we have a cycle here!
            if dp_labels[begin - 1] == 'n':
                option = dp[begin - 1]
                if cycle_length * num_of_repetitions <= (1 if begin != 1 else 0) + cycle_length + 1 + len(
                        str(num_of_repetitions)):
                    option += cycle_length * num_of_repetitions
                    if option <= dp[end]:
                        dp[end] = option
                        dp_directions[end] = begin - 1
                        dp_labels[end] = 'n'
                else:
                    option += (1 if begin != 1 else 0) + cycle_length + 1 + len(str(num_of_repetitions))
                    if option < dp[end]:
                        dp[end] = option
                        dp_directions[end] = begin - 1
                        dp_labels[end] = 'c'
                        dp_length_cycles[end] = cycle_length
            else:
                option = dp[begin - 1] + (1 if begin != 1 else 0)  # the +
                if cycle_length * num_of_repetitions <= cycle_length + 1 + len(str(num_of_repetitions)):
                    option += cycle_length * num_of_repetitions
                    if option <= dp[end]:
                        dp[end] = option
                        dp_directions[end] = begin - 1
                        dp_labels[end] = 'n'
                else:
                    option += cycle_length + 1 + len(str(num_of_repetitions))
                    if option < dp[end]:
                        dp[end] = option
                        dp_directions[end] = begin - 1
                        dp_labels[end] = 'c'
                        dp_length_cycles[end] = cycle_length

path = []

to_here = len(init_string) - 1
while to_here != 0:
    we_come_from = dp_directions[to_here]
    tag = dp_labels[to_here]
    cycle_length = 1 if tag == 'n' else dp_length_cycles[to_here]
    substr = init_string[we_come_from + 1: we_come_from + cycle_length + 1]
    path.append([substr, (to_here - we_come_from) // cycle_length, tag])
    to_here = we_come_from

path = path[::-1]
answer = ""

for i, item in enumerate(path):
    if i == 0:
        if item[2] == 'n':
            answer += item[0]
        else:
            answer += f"{item[0]}*{item[1]}"
    else:
        prev = path[i - 1]
        if item[2] == 'n':
            if prev[2] == 'n':
                answer += item[0]
            else:
                answer += f"+{item[0]}"
        else:
            answer += f"+{item[0]}*{item[1]}"

print(answer, file=open('output.txt', 'w'))
