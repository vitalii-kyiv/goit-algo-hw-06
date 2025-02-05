from collections import deque
from graph import G

def dfs_path(graph, start, goal, path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == goal:
        return path
    for neighbor in graph.neighbors(start):
        if neighbor not in path:
            new_path = dfs_path(graph, neighbor, goal, path)
            if new_path:
                return new_path
    return None

def bfs_path(graph, start, goal):
    queue = deque([(start, [start])])
    while queue:
        current, path = queue.popleft()
        for neighbor in graph.neighbors(current):
            if neighbor not in path:
                new_path = path + [neighbor]
                if neighbor == goal:
                    return new_path
                queue.append((neighbor, new_path))
    return None

start_node = "A"
goal_node = "I"
dfs_result = dfs_path(G, start_node, goal_node)
bfs_result = bfs_path(G, start_node, goal_node)

print(f"Шлях DFS ({start_node} -> {goal_node}): {dfs_result}")
print(f"Шлях BFS ({start_node} -> {goal_node}): {bfs_result}")

