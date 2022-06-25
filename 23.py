def get_smallest(dictionary):
    key = -1
    mn = float("inf")
    for curr_key in dictionary.keys():
        if not dictionary[curr_key]["visited"] and dictionary[curr_key]["path"] < mn:
            mn = dictionary[curr_key]["path"]
            key = curr_key
    return key


if __name__ == "__main__":
    n, s, f = map(int, input().split())
    s, f = s - 1, f - 1
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    graph = {}
    for i in range(n):
        graph[i] = {"kids": set(),
                    "path": float("inf"),
                    "visited": False}
    for u in range(n):
        for v in range(n):
            if matrix[u][v] >= 0 and u != v:
                graph[u]["kids"].add(v)
    graph[s]["path"] = 0
    smallest = s
    while smallest != -1:
        for key in graph[smallest]["kids"]:
            graph[key]["path"] = min(graph[smallest]["path"] + matrix[smallest][key], graph[key]["path"])
        graph[smallest]["visited"] = True
        smallest = get_smallest(graph)
    print(graph[f]["path"] if graph[f]["path"] != float("inf") else -1)
