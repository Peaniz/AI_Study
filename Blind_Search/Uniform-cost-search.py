import heapq  # Thư viện để sử dụng priority queue (hàng đợi ưu tiên)

graph = {
    'S': {'A': 3, 'B': 6, 'C': 2},
    'A': {'D': 3},
    'B': {'D': 4, 'E': 2, 'G': 9},
    'C': {'E': 1},
    'D': {'F': 5},
    'E': {'F': 6, 'H': 5},
    'F': {'G': 5},
    'G': {'H': 8},
    'H': {}
}

def UCS(initialState, goal):
    frontier = [(0, initialState)]  # Khởi tạo với chi phí là 0 cho đỉnh ban đầu
    explored = set()  # Để theo dõi các đỉnh đã duyệt
    path = {}  # Lưu lại đường đi (đỉnh cha -> đỉnh con)
    cost = {initialState: 0}  # Lưu chi phí đến mỗi đỉnh
    
    while frontier:
        current_cost, state = heapq.heappop(frontier)  # Lấy đỉnh có chi phí thấp nhất
        
        if state == goal:
            # Nếu tìm thấy đỉnh đích, tái tạo đường đi
            path_trace = []
            while state in path:
                path_trace.append(state)
                state = path[state]
            path_trace.append(initialState)
            path_trace.reverse()
            return path_trace, current_cost
        
        if state not in explored:
            explored.add(state)  # Đánh dấu đỉnh này đã được duyệt
            
            for neighbor, weight in graph[state].items():
                if neighbor not in explored:
                    new_cost = current_cost + weight
                    if neighbor not in cost or new_cost < cost[neighbor]:
                        # Nếu đỉnh chưa có trong cost hoặc tìm được đường đi ngắn hơn
                        cost[neighbor] = new_cost
                        heapq.heappush(frontier, (new_cost, neighbor))  # Thêm vào frontier
                        path[neighbor] = state  # Cập nhật đỉnh cha

    return None, None  # Nếu không tìm thấy đường đi

# Tìm đỉnh 'G' từ 'S'
result, total_cost = UCS('S', 'G')

if result:
    print(f"Path: {' -> '.join(result)}")
    print(f"Total Cost: {total_cost}")
else:
    print("404 Not Found!")
