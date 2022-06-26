def clean(string):
    new_string = ""
    for i in string.lower():
        if i not in ".,:;-'\"!?":
            new_string += i
        else:
            new_string += " "
    return new_string


n, m = map(int, input().split())
vocab, essay = set(), set()
for _ in range(n):
    vocab.add(input().strip().lower())
for _ in range(m):
    essay.update(clean(input()).split())

if vocab == essay:
    print("Everything is going to be OK.")
elif len(essay - vocab) > 0:
    print("Some words from the text are unknown.")
else:
    print("The usage of the vocabulary is not perfect.")
