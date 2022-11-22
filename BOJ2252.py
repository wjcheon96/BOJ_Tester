import sys
from collections import deque

f = open(sys.argv[1], "r")

N, M = map(int, f.readline().split())

height_list = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
queue = deque()

for _ in range(M):
    a, b = map(int, f.readline().split())
    height_list[a].append(b)
    indegree[b] += 1

for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)

sorting_box = []
while queue:
    target = queue.popleft()
    sorting_box.append(target)
    for i in height_list[target]:
        indegree[i] -= 1
        if indegree[i] == 0:
            queue.append(i)
print(*sorting_box)