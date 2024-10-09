class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight=1):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, weight))  # Lưu cặp (đỉnh, trọng số)

    def dls(self, node, goal, depth_limit, current_distance=0):
        print(f"Visiting Node: {node}, Depth Limit: {depth_limit}, Current Distance: {current_distance}")
        
        if node == goal:
            print(f"Goal {goal} found with distance {current_distance}")
            return True

        if depth_limit <= 0:
            return False

        for neighbor, weight in self.graph.get(node, []):
            # Gọi đệ quy, cộng dồn trọng số (distance)
            if self.dls(neighbor, goal, depth_limit - 1, current_distance + weight):
                return True

        return False

# Tạo đồ thị và thêm các cạnh với trọng số
graph = Graph()
graph.add_edge('A', 'B', 3)
graph.add_edge('A', 'C', 2)
graph.add_edge('B', 'D', 1)
graph.add_edge('B', 'E', 4)
graph.add_edge('C', 'F', 5)
graph.add_edge('C', 'G', 6)

start_node = 'A'
goal_node = 'F'
depth_limit = 3

# Tìm kiếm trong phạm vi độ sâu cho trước
if not graph.dls(start_node, goal_node, depth_limit):
    print(f"Goal {goal_node} was not found within depth limit {depth_limit}.")
