from controller import Controller

class UI:
    def __init__(self):
        self.__controller = Controller()

    def print_menu(self):
        print('\n0. Exit.')
        print('1. Get the number of vertices.')
        print('2. Parse the set of vertices.')
        print('3. Check if there is an edge between two given vertices.')
        print('4. Get the in and out degree of a specified vertex.')
        print('5. Parse the set of outbound edges of a vertex.')
        print('6. Parse the set of inbound edges of a vertex.')
        print('7. Modify the cost of a specified edge.')
        print('8. Add / remove an edge.')
        print('9. Add / remove a vertex.')
        print('10. Create random graph.')
        print('11. Read graph from file.')
        print('12. Find the connected components of the graph using a depth-first traversal of the graph.')
        print('13. Find the lowest cost walk between two given vertices.')
        print('14. Verify if the graph is DAG. If it is, find the highest cost path between two given vertices.')
        print('15. Find a covering of edges by vertices.')


    def run(self):
        self.__controller.save_random_graphs("random_graph1", "random_graph2")
        while True:
            self.print_menu()
            option = input('Your option:')
            while option.isnumeric() is False:
                print('Invalid input!')
                option = input('Your option:')
            option = int(option)
            if option == 11:
                file_name = input("Enter the file name:")
                self.__controller.create_graph_from_file(file_name)
            if option == 0:
                print("The modified graph is saved in output.txt.")
                self.__controller.save_graph_to_file("output")
                break
            if option == 1:
                print('\nThe number of vertices is', self.__controller.get_graph().number_of_vertices(), '.')
            elif option == 2:
                print('The set of vertices is', self.__controller.get_graph().get_set_of_vertices(), '.')
            elif option == 3:
                source = input('The source:')
                while source.isnumeric() is False or (source.isnumeric() is True and int(source) not in self.__controller.get_graph().get_set_of_vertices()):
                    if source.isnumeric() is False:
                        print('Invalid input!')
                    else:
                        print('This vertex does not exist!')
                    source = input('The source:')
                source = int(source)
                target = input('The target:')
                while target.isnumeric() is False or (target.isnumeric() is True and int(target) not in self.__controller.get_graph().get_set_of_vertices()):
                    if target.isnumeric() is False:
                        print('Invalid input!')
                    else:
                        print('This vertex does not exist!')
                target = int(target)

                result = self.__controller.get_graph().is_edge(source, target)
                if result == 0:
                    print("There is no edge from", source, "to", target, '.')
                else:
                    print("There is an edge!")
            elif option == 4:
                vertex = input('The vertex:')
                while vertex.isnumeric() is False or (vertex.isnumeric() is True and int(
                        vertex) not in self.__controller.get_graph().get_set_of_vertices()):
                    if vertex.isnumeric() is False:
                        print('Invalid input!')
                    else:
                        print('This vertex does not exist!')
                    vertex = input('The vertex:')
                vertex = int(vertex)
                print('The in degree of the vertex', vertex, 'is:', self.__controller.get_graph().in_degree_of_vertex(vertex))
                print('The out degree of the vertex', vertex, 'is:',
                       self.__controller.get_graph().out_degree_of_vertex(vertex))
            elif option == 5:
                vertex = input('The vertex:')
                while vertex.isnumeric() is False or (vertex.isnumeric() is True and int(
                        vertex) not in self.__controller.get_graph().get_set_of_vertices()):
                    if vertex.isnumeric() is False:
                        print('Invalid input!')
                    else:
                        print('This vertex does not exist!')
                    vertex = input('The vertex:')
                vertex = int(vertex)
                list = self.__controller.get_graph().out_neighbours(vertex)
                for neighbour in list:
                    print(vertex, neighbour)
            elif option == 6:
                vertex = input('The vertex:')
                while vertex.isnumeric() is False or (vertex.isnumeric() is True and int(
                        vertex) not in self.__controller.get_graph().get_set_of_vertices()):
                    if vertex.isnumeric() is False:
                        print('Invalid input!')
                    else:
                        print('This vertex does not exist!')
                    vertex = input('The vertex:')
                vertex = int(vertex)
                list = self.__controller.get_graph().in_neighbours(vertex)
                for neighbour in list:
                    print(neighbour, vertex)
            elif option == 7:
                s = input('The source:')
                while s.isnumeric() is False or (s.isnumeric() is True and int(
                        s) not in self.__controller.get_graph().get_set_of_vertices()):
                    if s.isnumeric() is False:
                        print('Invalid input!')
                    else:
                        print('This vertex does not exist!')
                    s = input('The source:')
                s = int(s)
                t = input('The target:')
                while t.isnumeric() is False or (t.isnumeric() is True and int(
                        t) not in self.__controller.get_graph().get_set_of_vertices()):
                    if t.isnumeric() is False:
                        print('Invalid input!')
                    else:
                        print('This vertex does not exist!')
                    t = input('The target:')
                t = int(t)
                new_cost = input("The new cost of the edge: ")
                if self.__controller.get_graph().is_edge(s, t) is False:
                    print("There is no edge between these two vertices!")
                else:
                    while new_cost.isnumeric() is False:
                        print('Invalid input!')
                        new_cost = input("The new cost of the edge: ")
                    self.__controller.get_graph().set_new_cost(s,t,new_cost)
                    print("Cost modified.")
            elif option == 8:
                opt2 = input('a. add edge \nb. remove edge\nChoice:')
                if opt2 == 'b':
                    s = input('The source:')
                    while s.isnumeric() is False or (s.isnumeric() is True and int(
                            s) not in self.__controller.get_graph().get_set_of_vertices()):
                        if s.isnumeric() is False:
                            print('Invalid input!')
                        else:
                            print('This vertex does not exist!')
                        s = input('The source:')
                    s = int(s)
                    t = input('The target:')
                    while t.isnumeric() is False or (t.isnumeric() is True and int(
                            t) not in self.__controller.get_graph().get_set_of_vertices()):
                        if t.isnumeric() is False:
                            print('Invalid input!')
                        else:
                            print('This vertex does not exist!')
                        t = input('The target:')
                    t = int(t)
                    if self.__controller.get_graph().is_edge(s, t) is False:
                        print("There is no edge between these two vertices!")
                    else:
                        self.__controller.get_graph().remove_edge(s, t)
                        print("Edge removed.")
                elif opt2 == 'a':
                    source = int(input('Source:'))
                    target = int(input('Target:'))
                    cost = int(input('Cost:'))
                    if self.__controller.get_graph().is_edge(source, target) is True:
                        print("The edge already exists!")
                    else:
                        self.__controller.get_graph().add_edge(source, target, cost)
            elif option == 9:
                opt2 = input('a. add vertex \nb. remove vertex\nChoice:')
                if opt2 == 'a':
                    v = int(input('Vertex number:'))
                    if v not in self.__controller.get_graph().get_set_of_vertices():
                        self.__controller.get_graph().add_vertex(v)
                        print('Vertex added.')
                    else:
                        print("This vertex already exists!")
                elif opt2 == 'b':
                    v = int(input('The vertex to be removed:'))
                    if v not in self.__controller.get_graph().get_set_of_vertices():
                        print("The vertex doesn't exist.")
                    else:
                        self.__controller.get_graph().remove_vertex(v)
                        print("Vertex removed.")
            elif option == 10:
                v = int(input('Vertices:'))
                e = int(input('Edges:'))
                self.__controller.save_graph(v, e, "random_graph")
                print("Graph saved in random_graph.txt.")
            elif option == 12:
                components = self.__controller.find_connected_components()
                for graph in components:
                    print('The graph is:')
                    if type(graph) == int:
                        print(graph)
                    else:
                        vertices = graph.get_set_of_vertices()
                        for key in vertices:
                            list = graph.out_neighbours(key)
                            for neighbour in list:
                                print(key, neighbour, graph.cost_of_an_edge(key, neighbour))
            elif option == 13:
                start = int(input('Starting vertex:'))
                end = int(input('Ending vertex:'))
                cost = self.__controller.backwards_Dijkstra(start, end)
                print('The cost is ', cost, '.')
            elif option == 14:
                topological_order = self.__controller.is_DAG()
                if topological_order == None:
                    print('The graph is not DAG.')
                else:
                    print('The graph is DAG. The topological order is:', topological_order)
                    v1 = int(input('Starting vertex:')) -1
                    v2 = int(input('Ending vertex:')) -1
                    dist = self.__controller.highest_cost_path(v1, v2)
                    #print('The path:', dist)
                    print('The cost is:', dist)

            elif option == 15:
                print(self.__controller.covering())

