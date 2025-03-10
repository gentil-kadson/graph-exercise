from grafo import Graph

graph = Graph()

graph.read_csv('./grafo_aula_dijkstra.csv')

distances, shortest_paths = graph.calculate_dijkstra('A')

for vertex, distance in distances.items():
    print(f"Shortest path from A to {vertex}: {distance} ({shortest_paths[vertex]}).")
