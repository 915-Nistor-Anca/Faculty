from random import randint

from directed_graph import Graph

from priority_queue import PriorityQueue, Data

class Controller:
    def __init__(self):
        self.__graph = Graph(0, 0)


    def create_graph_from_file(self, file_name):
        with open(file_name, "r") as file_pointer:
            k = 0
            edges = 0
            g = Graph(0, 0)
            for line in file_pointer:
                if k == 0:
                    x = line.split(' ')
                    vertices = int(x[0])
                    edges = int(x[1])
                    g = Graph(vertices, edges)
                    k += 1
                else:
                    x = line.split(' ')
                    g.add_edge2(int(x[0]), int(x[1]), int(x[2]))

        self.__graph = g


    def get_graph(self):
        return self.__graph

    def save_graph_to_file(self, file):
        with open(file, "w") as file_pointer:
            file_pointer.write(f"{self.__graph.number_of_vertices()} {self.__graph.number_of_edges()}")
            vertices = self.__graph.get_set_of_vertices()
            for key in vertices:
                list = self.__graph.out_neighbours(key)
                for neighbour in list:
                    file_pointer.write(f"\n{key} {neighbour} {self.__graph.cost_of_an_edge(key, neighbour)}")


    def generate_random_graph(self, vertices, edges):
        g = Graph(vertices, edges)
        for i in range(edges):
            x = randint(0, vertices-1)
            y = randint(0, vertices-1)
            while g.is_edge(x, y):
                x = randint(0, vertices-1)
                y = randint(0, vertices-1)
            g.add_edge2(x,y,randint(1, 100))
        return g


    def save_random_graphs(self, file1, file2):
        g1 = self.generate_random_graph(7, 20)
        g2 = self.generate_random_graph(6, 36)
        with open(file1, "w") as file_pointer:
            file_pointer.write(f"{g1.number_of_vertices()} {g1.number_of_edges()}")
            vertices = g1.get_set_of_vertices()
            for key in vertices:
                list = g1.out_neighbours(key)
                for neighbour in list:
                    file_pointer.write(f"\n{key} {neighbour} {g1.cost_of_an_edge(key, neighbour)}")
        with open(file2, "w") as file_pointer:
            file_pointer.write(f"{g2.number_of_vertices()} {g2.number_of_edges()}")
            vertices = g2.get_set_of_vertices()
            for key in vertices:
                list = g2.out_neighbours(key)
                for neighbour in list:
                   file_pointer.write(f"\n{key} {neighbour} {g2.cost_of_an_edge(key, neighbour)}")



    def save_graph(self, v, e, file):
        g1 = self.generate_random_graph(v, e)
        with open(file, "w") as file_pointer:
            file_pointer.write(f"{g1.number_of_vertices()} {g1.number_of_edges()}")
            vertices = g1.get_set_of_vertices()
            for key in vertices:
                list = g1.out_neighbours(key)
                for neighbour in list:
                    file_pointer.write(f"\n{key} {neighbour} {g1.cost_of_an_edge(key, neighbour)}")


    def depth_first_traversal(self, starting_vertex, visited_vertices, list_of_vertices, number_of_component):
    # The function receives a starting vertex and visits all the vertices which are connected to the initial one.
    # When a new vertex is visited, its value in "visited vertices"  becomes the number of the component it is part in.
        visited_vertices[starting_vertex] = number_of_component # it marks the vertex as visited
        for vertex in list_of_vertices: # it goes through all the vertices
            if self.__graph.is_edge(starting_vertex, vertex) and visited_vertices[vertex] == 0: # checks whether there exists an edge between the vertex and the one from the start
                self.depth_first_traversal(vertex, visited_vertices, list_of_vertices, number_of_component) #if there is an edge, the traversal starts again from the current vertex


    def find_connected_components(self):
        # This function returns a list of all the connected components of the graph.
        # It goes through all the vertices and checks if it was visited or not. If it wasn't, that means a new component
        # has been found and it starts the depth first traversal from it.
        # After all the vertices have been visited, the function checks again the vertices and groups them in components, wrt the value
        # which they have when they were checked as visited.
        #The last thing it does is to use the lists created and to form a graph for each connected component.
        list_of_vertices = self.__graph.get_set_of_vertices()
        visited_vertices = {}
        for vertex in list_of_vertices:
            visited_vertices[vertex] = 0
        number_of_components = 0
        for vertex in list_of_vertices:
            if visited_vertices[vertex] == 0:
                number_of_components += 1
                self.depth_first_traversal(vertex, visited_vertices, list_of_vertices, number_of_components)
        #in the first part, the algorithm "sorts" the vertices depending on which component they belong

        i = 1
        components = []
        while i <= number_of_components:
            component = []
            for vertex in list_of_vertices:
                if visited_vertices[vertex] == i:
                    component.append(vertex)
            components.append(component)
            i += 1
        # in the second part, it creates and saves the connected components

        final_graphs = []
        for component in components:
            #print(component)
            g1 = Graph(100, 100)

            for vertex in component:
                list_of_neighbours1 = self.__graph.out_neighbours(vertex)
                list2 = self.__graph.in_neighbours(vertex)
                for x in list2:
                    if x not in list_of_neighbours1:
                        list_of_neighbours1.append(x)

                if len(list_of_neighbours1) == 0:
                    final_graphs.append(vertex)
                else:
                    for v in list_of_neighbours1:
                        if self.__graph.is_edge(vertex, v):
                            g1.add_edge(vertex, v, self.__graph.cost_of_an_edge(vertex, v))
                        else:
                            g1.add_edge(v, vertex, self.__graph.cost_of_an_edge(vertex, v))
                    if g1 not in final_graphs:
                        final_graphs.append(g1)
            #in the third part, the algorithm creates graphs for each connected component

        return final_graphs

    def backwards_Dijkstra(self, starting_vertex, ending_vertex):
        visited = []
        q = PriorityQueue()
        next = {}
        dist = {}
        dist[ending_vertex] = 0
        found = False
        q.insert(Data(ending_vertex, 0))

        while not q.isEmpty() and not found:
            x = q.delete()
            if x in visited:
                return 0
            visited.append(x)
            print(x)
            for y in self.__graph.in_neighbours(x):
                if y not in dist.keys() or dist[y] + self.__graph.cost_of_an_edge(y, x) >= dist[x]:
                    dist[y] = dist[x] + self.__graph.cost_of_an_edge(y, x)
                    q.insert(Data(y, dist[y]))
                    next[x] = y
                    yy = y
            if x == starting_vertex:
                next[x] = yy
                found = True

        cost = 0
        for v in next.keys():
            cost = dist[v]
        return cost


    def topo_sort_DFS(self, x, sorted, fullyProcessed, inProcess):
        inProcess.add(x)
        for y in self.__graph.in_neighbours(x):
            if y in inProcess:
                return False
            elif y not in fullyProcessed:
                ok = self.topo_sort_DFS(y, sorted, fullyProcessed, inProcess)
                if not ok:
                    return False
        inProcess.remove(x)
        sorted.append(x+1)
        fullyProcessed.add(x)
        return True

    def is_DAG(self):
        sorted = []
        fullyProcessed = set()
        inProcess = set()
        for x in self.__graph.get_set_of_vertices():
            if x not in fullyProcessed:
                ok = self.topo_sort_DFS(x, sorted, fullyProcessed, inProcess)
                if not ok:
                    sorted  = None
                    return sorted
        return sorted


    def highest_cost_path(self, vertex1, vertex2):
        dist = dict()
        for vertex in self.__graph.get_set_of_vertices():
            dist[vertex] = 0

        dist[vertex1] = 0
        for u in self.is_DAG():
            if (u == vertex2):
                break

            adjacent = []
            #adjacent += self.__graph.in_neighbours(u)
            adjacent += self.__graph.out_neighbours(u)

            value = 0
            for v in adjacent:
                if v in self.__graph.out_neighbours(u):
                    value = self.__graph.cost_of_an_edge(u, v)
                else:
                    pass

                if dist[v] < dist[u] + value:
                    dist[v] = dist[u] + value
        #print('The path is', dist.keys())
        return dist[vertex2]


    def covering(self):
        all_vertices = self.__graph.get_set_of_vertices()
        solution = []
        edges = []
        for v in all_vertices:
            for v2 in self.__graph.in_neighbours(v):
                if (v2, v) not in edges:
                    edges.append((v2, v))
            for v2 in self.__graph.out_neighbours(v):
                if (v, v2) not in edges:
                    edges.append((v, v2))
        while all_vertices and edges:

            max_degree_vertex = 0
            degree = 0
            for v in all_vertices:
                if self.__graph.in_degree_of_vertex(v) + self.__graph.out_degree_of_vertex(v) > degree:
                    max_degree_vertex = v
                    degree = self.__graph.in_degree_of_vertex(v) + self.__graph.out_degree_of_vertex(v)

            solution.append(max_degree_vertex)
            for v in self.__graph.in_neighbours(max_degree_vertex):
                if (v, max_degree_vertex) in edges:
                    edges.remove((v, max_degree_vertex))
            for v in self.__graph.out_neighbours(max_degree_vertex):
                if (max_degree_vertex, v) in edges:
                    edges.remove((max_degree_vertex, v))
            all_vertices.remove(max_degree_vertex)


        return solution
