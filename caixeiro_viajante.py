import math

from grafo import Graph


graph = Graph()
graph.read_csv("grafo.csv")
graph.tsp_dfs("A", "A", ["A"], 0, ["A"], math.inf, [])

print(f"Menor custo: {graph.best_cost}")
print(f"Melhor caminho: {graph.best_path}")
