def AlphaBetaMinValue(node, alpha, beta, path=[]):
    if len(node.children) == 0:  # Leaf node
        return node, path
    node.value = 100000  # Set an initial high value
    best_path = []

    for child in node.children:
        temp, child_path = AlphaBetaMaxValue(child, alpha, beta, path + [node])
        if temp.value < node.value:
            node.value = temp.value
            best_path = child_path

        beta = min(beta, node.value)
        if alpha >= beta:
            break  # Alpha-Beta Pruning

    return node, best_path


def AlphaBetaMaxValue(node, alpha, beta, path=[]):
    if len(node.children) == 0:  # Leaf node
        return node, path
    node.value = -100000  # Set an initial low value
    best_path = []

    for child in node.children:
        temp, child_path = AlphaBetaMinValue(child, alpha, beta, path + [node])
        if temp.value > node.value:
            node.value = temp.value
            best_path = child_path

        alpha = max(alpha, node.value)
        if alpha >= beta:
            break  # Alpha-Beta Pruning

    return node, best_path


def AlphaBetaSearch(state):
    _, best_path = AlphaBetaMaxValue(state, float('-inf'), float('inf'))
    return best_path


class Tree:
    def __init__(self, data, cost=100000):
        self.value = None
        self.data = data
        self.cost = cost
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_data(self):
        return self.data

    def get_children(self):
        return self.children

    def get_parent(self):
        return self.parent

    def __lt__(self, other):
        return self.cost < other.cost


if __name__ == "__main__":
    # Creating the tree structure
    A = Tree("A")
    B = Tree("B")
    C = Tree("C")
    D = Tree("D")
    E = Tree("E")
    F = Tree("F")
    G = Tree("G")
    H = Tree("H")
    I = Tree("I")
    J = Tree("J")
    K = Tree("K")
    L = Tree("L")
    M = Tree("M")
    N = Tree("N")
    Z = Tree("Z")

    # Adding children
    A.add_child(B)
    A.add_child(C)
    B.add_child(D)
    B.add_child(E)
    C.add_child(F)
    C.add_child(G)
    D.add_child(H)
    D.add_child(I)
    E.add_child(J)
    E.add_child(K)
    F.add_child(M)
    F.add_child(N)
    G.add_child(L)
    G.add_child(Z)

    # Assigning values to leaf nodes
    H.value = 2
    I.value = 9
    J.value = 7
    K.value = 4
    M.value = 8
    N.value = 9
    L.value = 3
    Z.value = 5

    # Perform AlphaBeta Search
    path = AlphaBetaSearch(A)

    # Print the optimal path
    print("Optimal path:", " -> ".join([node.data for node in path]))
    print(f"Optimal value: {A.value}")
