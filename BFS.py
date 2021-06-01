class Graph:
    def __int__(self, edges):
        self.edges = edges
        self.graph_dict = {}

        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print(self.graph_dict)

if __name__ = '__main__':

    routes = [
        ['A', 'B'],
        ['A', 'D'],
        ['B', 'A'],
        ['B', 'C'],
        ['C', 'B'],


    ]
