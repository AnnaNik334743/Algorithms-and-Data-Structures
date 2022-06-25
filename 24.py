class Vertex:
    def __init__(self, key, dist=float('inf'), prev=None):
        self.key = key
        self.dist = dist
        self.prev = prev


class Edge:
    def __init__(self, start, end, length):
        self.start = start
        self.end = end
        self.length = length


class Graph:
    def __init__(self):
        self.vertexes = {}
        self.edges = []

    def construct_from_edges(self, num_vert, list_of_edges):
        for i in range(1, num_vert + 1):
            self.vertexes[i] = Vertex(i)
        for tup in list_of_edges:
            start, end, length = tup
            vert1 = self.find_vertex(start)
            # if vert1 == -1:
            #     vert1 = Vertex(start)
            vert2 = self.find_vertex(end)
            # if vert2 == -1:
            #     vert2 = Vertex(end)
            edge = Edge(vert1, vert2, length)
            # self.vertexes[start] = vert1
            # self.vertexes[end] = vert2
            self.edges.append(edge)

    def find_vertex(self, key):
        try:
            vertex = self.vertexes[key]
            return vertex
        except KeyError:
            return -1

    def bellman_ford(self, s):
        start_vertex = self.find_vertex(s)
        if start_vertex == -1:
            raise Exception("There is no such vertex")
        start_vertex.dist = 0
        for _ in range(len(self.vertexes) - 1):
            for edge in self.edges:
                if edge.end.dist > edge.start.dist + edge.length:
                    edge.end.dist = edge.start.dist + edge.length
                    edge.end.prev = edge.start


if __name__ == "__main__":
    n, m = map(int, input().split())
    list_of_edges = []
    for _ in range(m):
        u, v, l = map(int, input().split())
        list_of_edges.append((u, v, l))
    graph = Graph()
    graph.construct_from_edges(n, list_of_edges)
    graph.bellman_ford(1)
    for i in range(1, n + 1):
        vertex = graph.find_vertex(i)
        print(vertex.dist if vertex != -1 and vertex.dist != float('inf') else 30000, end=' ')
