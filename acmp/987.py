i = int
s = print
p = ''
t = []
for l in open(0).readlines():
    if 'g' in l:
        p = l.split()[1]
    elif 'u' not in l:
        t.append(i(l.split('=')[1]))
a = len(t)
s(f"Ping statistics for {p}:\nPackets: Sent = 4 Received = {a} Lost = {4 - a} ({i((4 - a) * 25)}% loss)")
if a != 0:
    s(f"Approximate round trip times:\nMinimum = {min(t)} Maximum = {max(t)} Average = {i(sum(t) / a + 0.5)}")
