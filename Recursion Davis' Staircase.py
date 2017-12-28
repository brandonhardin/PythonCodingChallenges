from collections import deque

nmax = 36
d = deque([0, 0, 1], nmax + 1)
for _ in range(nmax):
    d.append(d[-3] + d[-2] + d[-1])

for _ in range(int(input())):
    print(d[int(input())])