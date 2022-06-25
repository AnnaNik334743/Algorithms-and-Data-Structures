from collections import deque

if __name__ == "__main__":
    n = int(input())
    matrix = []
    for _ in range(n):
        matrix.append(list(input().split()))
    graph = {}
    for i in range(n):
        graph[i] = {"kids": set(),
                    "visited": False,
                    "path": float("inf")}
    for u in range(n):
        for v in range(n):
            if matrix[u][v] == "1":
                graph[u]["kids"].add(v)
                graph[v]["kids"].add(u)
    start, end = map(int, input().split())
    start, end = start - 1, end - 1
    graph[start]["path"] = 0
    queue = deque()
    queue.append(start)
    while len(queue) > 0:
        u = queue.popleft()
        for v in graph[u]["kids"]:
            if graph[v]["path"] == float("inf"):
                queue.append(v)
                graph[v]["path"] = graph[u]["path"] + 1
    print(graph[end]["path"] if graph[end]["path"] != float("inf") else -1)
