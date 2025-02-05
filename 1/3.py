from graph import G
import heapq

def dijkstra(graph, start):
    shortest_paths = {node: float('inf') for node in graph.nodes}
    shortest_paths[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > shortest_paths[current_node]:
            continue
        
        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            distance = current_distance + weight
            
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return shortest_paths

dijkstra_result = {node: dijkstra(G, node) for node in G.nodes}

print("\nНайкоротші шляхи за алгоритмом Дейкстри від кожної вершини:")
for node, paths in dijkstra_result.items():
    print(f"Від {node}: {paths}")