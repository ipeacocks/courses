class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []

class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

class Graph(object):
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def insert_node(self, new_node_val):
        new_node = Node(new_node_val)
        self.nodes.append(new_node)
        
    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        from_found = None
        to_found = None

        for node in self.nodes:
            if node_from_val == node.value:
                from_found = node
            if node_to_val == node.value:
                to_found = node

        if from_found == None:
            from_found = Node(node_from_val)
            self.nodes.append(from_found)

        if to_found == None:
            to_found = Node(node_to_val)
            self.nodes.append(to_found)

        new_edge = Edge(new_edge_val, from_found, to_found)
        from_found.edges.append(new_edge)
        to_found.edges.append(new_edge)
        self.edges.append(new_edge)

    def get_edge_list(self):
        return [(edge.value, edge.node_from.value, edge.node_to.value) for edge in self.edges]

    def get_adjacency_list(self):
        result_list = []
        list_edges = self.get_edge_list()

        for i in range(len(self.edges) + 1):
            result_list.append([])

        for edge in list_edges:
            result_list[edge[1]].append((edge[2], edge[0]))

        for i in range(len(result_list)):
            if not result_list[i]:
                result_list[i] = None

        return result_list
    
    def get_adjacency_matrix(self):
        result_list = []
        list_edges = self.get_adjacency_list()

        for list_ in list_edges:
            if not list_:
                result_list.append([0 for i in range(len(list_edges))])
            else:
                template = [0 for i in range(len(list_edges))]
                for tuple_ in list_:
                    template[tuple_[0]] = tuple_[1]
                result_list.append(template)

        return result_list

graph = Graph()
graph.insert_edge(100, 1, 2)
graph.insert_edge(101, 1, 3)
graph.insert_edge(102, 1, 4)
graph.insert_edge(103, 3, 4)

# Should be [(100, 1, 2), (101, 1, 3), (102, 1, 4), (103, 3, 4)]
print graph.get_edge_list()
print "-" * 10

# Should be [None, [(2, 100), (3, 101), (4, 102)], None, [(4, 103)], None]
print graph.get_adjacency_list()
print "-" * 10

# Should be [[0, 0, 0, 0, 0], [0, 0, 100, 101, 102], [0, 0, 0, 0, 0], [0, 0, 0, 0, 103], [0, 0, 0, 0, 0]]
print graph.get_adjacency_matrix()