from collections import deque


def is_tree(graph, key):
    queue = deque()
    queue.append(key)
    while len(queue) != 0:
        curr_key = queue.popleft()
        if graph[curr_key]["visited"]:
            return False
        graph[curr_key]["visited"] = True
        for kid_key in graph[curr_key]["kids"]:
            graph[kid_key]["kids"].remove(curr_key)
        queue.extend(graph[curr_key]["kids"])
    return True


n = int(input())
matrix = []
count = 0
for _ in range(n):
    matrix.append(input().split())

graph = {i: {"kids": [], "visited": False} for i in range(n)}
for i in range(n):
    for j in range(i+1, n):
        if matrix[i][j] == '1':
            graph[i]["kids"].append(j)
            graph[j]["kids"].append(i)
            count += 1

print("YES" if count == n-1 and is_tree(graph, 0) else "NO")
