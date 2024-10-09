graph = {

    'S': {'A': 3, 'B': 6, 'C': 2},
    'A': {'D': 3},
    'B': {'D': 4, 'E': 2, 'G':9},
    'C': {'E': 1},
    'D': {'F': 5},
    'E': {'F': 6, 'H': 5},
    'F': {'G': 5},
    'G': {'H': 8},
    'H': {}
}

def DFS(initialState, goal):
    frontier = [(initialState, 0)]  # Mỗi phần tử sẽ là (đỉnh, khoảng cách từ đỉnh ban đầu)
    explored = []

    while frontier:
        state, distance = frontier.pop()  # DFS sử dụng ngăn xếp (LIFO), pop từ cuối danh sách
        explored.append((state, distance))  # Lưu cả đỉnh và khoảng cách

        # Kiểm tra nếu tìm thấy đỉnh đích
        if goal == state:
            return explored

        # Duyệt qua các đỉnh liền kề
        for neighbor, weight in graph[state].items():
            # Kiểm tra nếu neighbor chưa có trong explored hoặc frontier
            if neighbor not in [x[0] for x in explored] and neighbor not in [x[0] for x in frontier]:
                frontier.append((neighbor, distance + weight))  # Cộng dồn khoảng cách

    return False

# Tìm đỉnh 'G' từ 'S'
result = DFS('S', 'G')

if result:
    print('explored (vertex, distance):')
    for vertex, dist in result:
        print(f'{vertex}: {dist}')
else:
    print("404 Not Found!")
