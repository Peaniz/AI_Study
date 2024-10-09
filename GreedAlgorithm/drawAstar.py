import heapq
import matplotlib.pyplot as plt
import networkx as nx


class Node:
    def __init__(self, label, goal_cost):
        self.label = label
        self.cost = 10000  # Initial cost (infinity)
        self.goal_cost = goal_cost  # Heuristic value (goal estimate)
        self.save_cost = None
        self.parent = None  # Parent reference for path reconstruction
        self.child = []

    def __repr__(self):
        return str(dict({
            "label": self.label,
            "cost": self.cost,
            "goal cost": self.goal_cost
        }))

    def __eq__(self, other):
        return self.label == other.label

    def __lt__(self, other):
        # Priority queue will use only goal_cost (heuristic)
        return self.goal_cost < other.goal_cost

    def get_label(self):
        return self.label

    def neighbors(self):
        return self.child


class Tree:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_nodes(self, data):
        for node in data:
            self.nodes.append(node)

    def add_node(self, node):
        self.nodes.append(node)

    def get_index(self, node):
        for i, n in enumerate(self.nodes):
            if n.get_label() == node.get_label():
                return i
        return -1

    def add_edges(self, tuple_edges):
        for t in tuple_edges:
            start_label = t[0]
            end_label = t[1]
            w = t[2]
            index_start_label = self.get_index(Node(start_label, None))
            index_end_label = self.get_index(Node(end_label, None))
            self.nodes[index_start_label].child.append(self.nodes[index_end_label])
            self.nodes[index_end_label].parent = self.nodes[index_start_label]
            self.edges.append((self.nodes[index_start_label], self.nodes[index_end_label], t[2]))

    def show_nodes(self):
        return {node.get_label(): [n.get_label() for n in node.neighbors()] for node in self.nodes}

    def get_edge(self, start_node, end_node):
        try:
            return [edges for edges in self.edges if edges[0] == start_node and edges[1] == end_node][0]
        except:
            return None


def update_cost(tree, current_node, prev_node):
    # In Greedy Best First Search, we don't update the cost, since it's based on heuristics
    pass


def Greedy_Best_First_Search(tree, start, end):
    frontier = [start]
    heapq.heapify(frontier)
    explored = []

    while len(frontier) > 0:
        state = heapq.heappop(frontier)
        explored.append(state)
        print(f"Exploring: {state.label}")

        if state == end:
            return explored

        for child in state.neighbors():
            # We don't update the cost here since Greedy Best First Search is heuristic-based
            if child.get_label() not in list(set(node.get_label() for node in frontier + explored)):
                heapq.heappush(frontier, child)

    return False


def print_shortest_path(end):
    path = []
    current_node = end
    while current_node is not None:
        path.append(current_node.label)
        current_node = current_node.parent
    return path[::-1]  # Reverse the path to get from start to end


def plot_graph(tree, shortest_path):
    G = nx.Graph()

    # Add nodes and edges to the graph
    for node in tree.nodes:
        G.add_node(node.get_label())

    for edge in tree.edges:
        G.add_edge(edge[0].get_label(), edge[1].get_label(), weight=edge[2])

    # Draw the graph
    pos = nx.spring_layout(G)
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color='skyblue', font_size=10, font_weight='bold')

    # Highlight the shortest path
    path_edges = [(shortest_path[i], shortest_path[i + 1]) for i in range(len(shortest_path) - 1)]
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=3)

    plt.title("Greedy Best First Search - Shortest Path")
    plt.show()


if __name__ == "__main__":
    tree = Tree()
    tree.add_nodes([
        Node("A", 6), Node("B", 3), Node("C", 4), Node("D", 5),
        Node("E", 3), Node("F", 1), Node("G", 6), Node("H", 2),
        Node("I", 5), Node("J", 4), Node("K", 2), Node("L", 0),
        Node("M", 4), Node("N", 0), Node("O", 4)
    ])

    tree.add_edges([
        ("A", "B", 2), ("A", "C", 1), ("A", "D", 3), ("B", "E", 5),
        ("B", "F", 4), ("C", "G", 6), ("C", "H", 3), ("D", "I", 2),
        ("D", "J", 4), ("F", "K", 2), ("F", "L", 1), ("F", "M", 4),
        ("H", "N", 2), ("H", "O", 4)
    ])

    print("Danh sách đỉnh và các đỉnh kề tương ứng:")
    print(tree.show_nodes())

    result = Greedy_Best_First_Search(tree, tree.nodes[0], tree.nodes[14])

    if result:
        s = "Explored nodes: "
        for node in result:
            s += node.label + " "
        print(s)

        # Print the shortest path
        path = print_shortest_path(tree.nodes[14])
        print("Shortest path: ", " -> ".join(path))
        print(f"Goal cost: {tree.nodes[14].goal_cost}")

        # Plot the graph and highlight the shortest path
        plot_graph(tree, path)
    else:
        print("404 Not Found!")
