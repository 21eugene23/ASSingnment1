class Graph:
    def __init__(self):
        self.directed = directed

        self.adj_list= dict()

    def __repr__(self):
        graph_str= ""

        for node, neighbours in self.adj_list:
            graph_str += f"{node}  --> {neighbours} /n"

    def obtain_neighbours(self):
        pass
    def adj_matrix(self):
        pass

    def add_node(self,node):

        if node not in self.adj_list:
            self.adj_list[node]= set()
        else:
            raise ValueError("Node already exists")

    def add_edge(self,from_node,to_node,weight=None):

        if from_node not in self.adj_list:
            self.add_node(to_node)

        if to_node not in self.adj_list:
            self.add_node(to_node)

        if weight is None:

            self.adj_list[from_node].add[to_node]
        else:
            self.adj_list[from_node].add[(to_node,weight)]

        if not self.directed:
            self.adj_list[to_node].add[(from_node,weight)]



    def depth_first_search(self):
        pass

    def breadth_first_search(self):
        pass