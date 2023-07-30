def find_way(graph, start, end, way=[]):
    way = way + [start]
    if start == end:
        return [way]
    if start not in graph:
        return []
    ways = []
    for node in graph[start]:
        if node not in way:
            new_ways = find_way(graph, node, end, way)
            for new_way in new_ways:
                ways.append(new_way)
    return ways


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
start = 'A'
end = 'F'
ways = find_way(graph, start, end)
print("Все пути от вершины", start, "до вершины", end, "в графе:")
for way in ways:
    print(way)
