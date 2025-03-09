import networkx as nx
import matplotlib.pyplot as plt

from grafo import Graph


graph = Graph()
graph.read_csv("grafo.csv")
graph.tsp_dfs("A", "A", ["A"], 0, ["A"])

print(f"Menor custo: {graph.best_cost}")
print(f"Melhor caminho: {graph.best_path}")

G = nx.Graph()
edges: list[tuple[str|int, str|int, int]] = []

for vertex, adjacents in graph.vertices.items():
    adjacent = adjacents.head
    while adjacent:
        edges.append(
            (vertex, adjacent.data, adjacent.weight)
        )
        adjacent = adjacent.next

G.add_weighted_edges_from(edges)
position = nx.spring_layout(G, seed=42)
plt.figure(figsize=(8, 6))

nx.draw(
    G, 
    position, 
    with_labels=True, 
    node_color='lightblue', 
    edge_color='gray', 
    node_size=2000, 
    font_size=12, 
    font_weight='bold'
)
highlighted_edges = [
    (graph.best_path[i], current)
    for i, current in enumerate(graph.best_path[1:])
]
nx.draw_networkx_edges(G, position, highlighted_edges, edge_color='red', width=3)

edge_weights = {(fron, to): weight for fron, to, weight in edges}
nx.draw_networkx_edge_labels(G, position, edge_labels=edge_weights, font_size=10)

plt.title("TSP Brute-Force Solution")
plt.show()
