import networkx as nx
import matplotlib.pyplot as plt

# Định nghĩa đồ thị
V = ["S", "A", "B", "C", "D", "E", "F", "G", "H"]
E = [("S", "A"), ("S", "B"), ("S", "C"), ("A", "B"), ("A", "D"), ("B", "C"), ("B", "D"),
     ("B", "F"), ("B", "G"), ("C", "F"), ("D", "E"), ("E", "F"), ("E", "G"), ("F", "H"), ("H", "G")]

# Tạo đồ thị bằng networkx
graph = nx.Graph()
graph.add_edges_from(E)

# Hàm BFS
def BFS(initialState, goal):
    frontier = [(initialState, 0)]  # Mỗi phần tử là (đỉnh, khoảng cách từ đỉnh ban đầu)
    explored = []
    parent = {initialState: None}  # Lưu các đỉnh cha để vẽ đường đi

    while frontier:
        state, distance = frontier.pop(0)  # Lấy đỉnh và khoảng cách từ hàng đợi
        explored.append((state, distance))  # Lưu lại đỉnh và khoảng cách
        if goal == state:  # Nếu đỉnh là mục tiêu
            path = []
            while state is not None:  # Lấy lại đường đi từ đỉnh goal về đỉnh bắt đầu
                path.append(state)
                state = parent[state]
            return path[::-1]  # Đảo ngược lại đường đi
        for neighbor in graph[state]:  # Lấy các đỉnh kề của đỉnh hiện tại
            if neighbor not in parent:
                parent[neighbor] = state
                frontier.append((neighbor, distance + 1))  # Cộng dồn khoảng cách
    return False

# Chạy BFS để tìm đường đi từ "S" đến "G"
path = BFS('S', 'G')

# Trực quan hóa đồ thị và đường đi
if path:
    # Vẽ đồ thị
    pos = nx.spring_layout(graph)  # Định dạng vị trí các đỉnh
    plt.figure(figsize=(8, 6))
    nx.draw(graph, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=12, font_weight='bold', edge_color='gray')

    # Vẽ đường đi tìm được
    path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
    nx.draw_networkx_edges(graph, pos, edgelist=path_edges, edge_color='red', width=2)

    plt.title('BFS Path from S to G')
    plt.show()
else:
    print("404 Not Found!")
