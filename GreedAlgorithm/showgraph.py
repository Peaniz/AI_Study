import matplotlib.pyplot as plt
import networkx as nx

# Khởi tạo các nút với label và goal_cost
nodes = {
    "A": 6, "B": 3, "C": 4, "D": 5, "E": 3, "F": 1, "G": 6, "H": 2,
    "I": 5, "J": 4, "K": 2, "L": 0, "M": 4, "N": 8, "O": 4
}

# Khởi tạo các mối quan hệ giữa các nút
edges = [
    ("A", "B"), ("A", "C"), ("A", "D"), ("B", "E"), ("B", "F"),
    ("C", "G"), ("C", "H"), ("D", "I"), ("D", "J"), ("F", "K"),
    ("F", "L"), ("F", "M"), ("H", "N"), ("H", "O")
]

# Tạo đồ thị
G = nx.Graph()
G.add_nodes_from(nodes.keys())
G.add_edges_from(edges)

# Vẽ đồ thị
pos = nx.spring_layout(G)  # Tự động sắp xếp các nút
plt.figure(figsize=(10, 10))
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=12, font_weight="bold", edge_color="gray")

# Hiển thị trọng số của các nút (goal_cost)
for node, goal_cost in nodes.items():
    plt.text(pos[node][0], pos[node][1] + 0.05, str(goal_cost), fontsize=12, ha='center', color='red')

plt.title("Greedy Best-First Search (GBF) Visualization")
plt.show()
