import heapq

class Node:
    def __init__(self, label, goal_cost):
        self.label = label
        self.cost = 10000  # Initialize cost to a high value
        self.goal_cost = goal_cost
        self.save_cost = None
        self.pr = []  # List of parent nodes
        self.chld = []  # List of child nodes

    def __repr__(self):
        return str({
            "label": self.label,
            "cost": self.cost,
            "goal_cost": self.goal_cost
        })

    def __eq__(self, other):
        return self.label == other.label

    def __lt__(self, other):
        return self.goal_cost < other.goal_cost

    def get_label(self):
        return self.label

    def neighbors(self):
        return self.chld + self.pr

    def get_children(self):
        return self.chld

def update_frontier(frontier, new_node):
    for idx, n in enumerate(frontier):
        if n == new_node:
            if frontier[idx].goal_cost > new_node.goal_cost:
                frontier[idx] = new_node

def GBF_search(initial_state, goalTest):
    frontier = []
    explored = []

    heapq.heapify(frontier)
    heapq.heappush(frontier, initial_state)

    while len(frontier) > 0:
        state = heapq.heappop(frontier)
        explored.append(state)

        if goalTest(state):
            return explored

        for neighbor in state.get_children():
            if neighbor not in frontier and neighbor not in explored:
                heapq.heappush(frontier, neighbor)
            elif neighbor in frontier:
                update_frontier(frontier, neighbor)

    return False

if __name__ == "__main__":
    A = Node("A", 6)
    B = Node("B", 3)
    C = Node("C", 4)
    D = Node("D", 5)
    E = Node("E", 3)
    F = Node("F", 1)
    G = Node("G", 6)
    H = Node("H", 2)
    I = Node("I", 5)
    J = Node("J", 4)
    K = Node("K", 2)
    L = Node("L", 0)
    M = Node("M", 4)
    N = Node("N", 8)
    O = Node("O", 4)

    A.chld.extend([B, C, D])
    B.chld.extend([E, F])
    C.chld.extend([G, H])
    D.chld.extend([I, J])
    F.chld.extend([K, L, M])
    H.chld.extend([N, O])

    result = GBF_search(A, lambda x: x == L)
    total_cost = 0
    if result:
        print("Explored:")
        for i in result:
            total_cost += i.goal_cost
            print(i.label + " " + str(total_cost))
    else:
        print("404 Not Found!")
