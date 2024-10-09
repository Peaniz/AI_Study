V = ["S", "A", "B", "C", "D", "E", "F", "G", "H"]
E = [("S", "A"), ("S", "B"), ("S", "C"), ("A", "B"), ("A", "D"), ("B", "C"), ("B", "D"), ("B", "F"), ("B", "G"), ("C", "F"), ("D", "E"), ("E", "F"), ("E", "G"), ("F", "H"), ("H", "G")]

graph = {}
for vertex in V:
    graph[vertex] = []
for edge in E:
    u= edge[0]
    v = edge[1]
    graph[u].append(v)
    graph[v].append(u)

print("Danh sách đỉnh và các đỉnh kề tương ứng:")
for vertex in V:
    print(f"{vertex}: {graph[vertex]}")


def BFS(initialState, goal):
    frontier = [(initialState, 0)]  # Mỗi phần tử là (đỉnh, khoảng cách từ đỉnh ban đầu)
    explored = []

    while frontier:
        state, distance = frontier.pop(0)  # Lấy đỉnh và khoảng cách từ hàng đợi
        explored.append((state, distance))  # Lưu lại đỉnh và khoảng cách
        if goal == state:  # Nếu đỉnh là mục tiêu
            return explored
        for neighbor in graph[state]:  # Lấy các đỉnh kề của đỉnh hiện tại
            if neighbor not in [x[0] for x in explored] and neighbor not in [x[0] for x in frontier]:
                frontier.append((neighbor, distance + 1))  # Cộng dồn khoảng cách
    return False


result = BFS('S', 'G')

if result:
    print('Thu tu dinh kham pha:')
    # Sử dụng join để nối các phần tử thành một chuỗi
    print(' -> '.join([f'{vertex[0]}({vertex[1]})' for vertex in result]))

else:
    print("404 Not Found!")