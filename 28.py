from collections import deque


def friends(graph, key):
    queue = deque()
    queue.append(key)
    count = -1
    while len(queue) != 0:
        curr_key = queue.popleft()
        if not graph[curr_key]["visited"]:
            graph[curr_key]["visited"] = True
            count += 1
            queue.extend(graph[curr_key]["kids"])
    return count


n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(input().split())

graph = {i: {"kids": [], "visited": False} for i in range(n)}
for i in range(n):
    for j in range(i+1, n):
        if matrix[i][j] == '1':
            graph[i]["kids"].append(j)
            graph[j]["kids"].append(i)

print(friends(graph, m-1))
