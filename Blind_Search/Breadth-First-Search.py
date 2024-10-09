graph = {

    'S': {'A': 3, 'B': 6, 'C': 2},
    'A': {'D': 3},
    'B': {'D': 4, 'E': 2, 'G':9},
    'C': {'E': 1},
    'D': {'F': 5},
    'E': {'F': 6, 'H': 5},
    'F': {'G': 5},
    'G': {'H': 8}
}


def BFS(initialState, goal):
    frontier = [(initialState, 0)]  # Mỗi phần tử sẽ là (đỉnh, khoảng cách từ đỉnh ban đầu)
    explored = []
    
    while frontier:
        state, distance = frontier.pop(0)  # Lấy đỉnh và khoảng cách ra khỏi hàng đợi
        explored.append((state, distance))  # Lưu cả đỉnh và khoảng cách
        if goal == state:
            return explored
        for neighbor, weight in graph[state].items():  # neighbor là đỉnh liền kề, weight là khoảng cách
            if neighbor not in [x[0] for x in (explored and frontier)]:
                frontier.append((neighbor, distance + weight))  # Cộng dồn khoảng cách
    return False

result = BFS('S', 'G')

if result:
    print('explored (vertex, distance):')
    for vertex, dist in result:
        print(f'{vertex}: {dist}')
else:
    print("404 Not Found!")
