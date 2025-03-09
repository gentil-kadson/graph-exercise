from grafo import Graph

graph = Graph()

graph.read_csv('./grafo_aula_dijkstra.csv')

shortes_path = graph.calculate_dijkstra('A')

for destiny, distance in shortes_path.items():
    print(f"Shortest path from A to {destiny}: {distance}")

graph.draw_graph()