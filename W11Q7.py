import heapq

def dijkstra(graph, start, target):
    pq = [(0, start, [start])]
    visited = set()

    while pq:
        (dist, current, path) = heapq.heappop(pq)

        if current in visited:
            continue
        visited.add(current)

        if current == target:
            return dist, path

        for neighbor, weight in graph.get(current, []):
            if neighbor not in visited:
                heapq.heappush(pq, (dist + weight, neighbor, path + [neighbor]))

    return float("inf"), []  # If no path exists

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

start_node = 'A'
target_node = 'D'
distance, path = dijkstra(graph, start_node, target_node)

print(f"Shortest distance from {start_node} to {target_node}: {distance}")
print(f"Path: {' -> '.join(path)}")