from grafo import Graph

graph = Graph()

graph.read_csv('./grafo_aula_dijkstra.csv')

origin = input("Where are you at? ")
destination = input("Where do you want to go? ")

distances, shortest_paths = graph.calculate_dijkstra(origin)

for vertex, distance in distances.items():
    if vertex == destination:
        print(f"Shortest path from {origin} to {vertex}: {distance} ({shortest_paths[vertex]}).")
