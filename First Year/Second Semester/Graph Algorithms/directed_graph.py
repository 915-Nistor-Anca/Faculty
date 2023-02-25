import copy

class Graph:
    def __init__(self, vertices, edges):
        self.__din = {}
        self.__dout = {}
        self.__dcosts = {}
        self.___vertices = vertices
        self.__edges = edges
        for vertex in range(vertices):
            self.__din[vertex] = []
            self.__dout[vertex] = []

    def add_edge2(self, source, target, cost):
        if target not in self.__dout[source]:
            self.__dout[source].append(target)
            self.__din[target].append(source)
            self.__dcosts[(source, target)] = cost

    def add_edge(self, source, target, cost):
        if source in self.__dout.keys():
            if target not in self.__dout[source]:
                self.__dout[source].append(target)
                self.__din[target].append(source)
                self.__dcosts[(source, target)] = cost
                self.__edges += 1

    def remove_edge(self, source, target):
        if self.is_edge(source, target):
            self.__dout[source].remove(target)
            self.__din[target].remove(source)
            del self.__dcosts[(source, target)]

    def add_vertex(self, vertex):
        self.___vertices += 1
        self.__din[vertex] = []
        self.__dout[vertex] = []

    def remove_vertex(self, vertex):
        self.___vertices -= 1
        for e in self.__dout[vertex]:
            self.__din[e].remove(vertex)
            self.__dout[vertex].remove(e)
            del self.__dcosts[(vertex, e)]
        del self.__dout[vertex]
        for e in self.__din[vertex]:
            self.__dout[e].remove(vertex)
            self.__din[vertex].remove(e)
            del self.__dcosts[(e, vertex)]
        del self.__din[vertex]




    def get_set_of_vertices(self):
        list_of_vertices = []
        for key in self.__din:
            list_of_vertices.append(key)
        return list_of_vertices

    def is_edge(self, source, target):
        if target in self.__din.keys():
            return source in self.__din[target]

    def in_degree_of_vertex(self, vertex):
        return len(copy.copy(self.__din[vertex]))

    def out_degree_of_vertex(self, vertex):
        return len(copy.copy(self.__dout[vertex]))

    def in_neighbours(self, vertex):
        if vertex in self.__din.keys():
            return copy.copy(self.__din[vertex])

    def out_neighbours(self, vertex):
        if vertex in self.__dout:
            return copy.copy(self.__dout[vertex])
        return None

    def cost_of_an_edge(self, source, target):
        if self.is_edge(source, target):
            return self.__dcosts[(source, target)]

    def set_new_cost(self, source, target, new_cost):
        self.__dcosts[(source, target)] = new_cost

    def number_of_vertices(self):
        return self.___vertices

    def number_of_edges(self):
        return self.__edges

