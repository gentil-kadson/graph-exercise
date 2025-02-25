from threading import Thread
import networkx as nx
import matplotlib.pyplot as plt

from grafo import Graph


graph = Graph()
graph.read_csv("grafo.csv")

G = nx.Graph()

for vertex, adjacent in graph.vertices.items():
    current = adjacent.head
    while current:
        G.add_edge(vertex, current.data, weight=current.weight)
        current = current.next

print(24 * "=")
print("Exploração do Mapa")
print(24 * "=")

def interact_with_map():
    while True:
        starting_vertex: str = input("De onde você deseja começar? ")
        if starting_vertex not in graph.vertices:
            print("Esse local não está no grafo")
            continue

        finishing_vertex: str = input("Para onde você deseja ir? ")
        if finishing_vertex not in graph.vertices:
            print("Esse local não está no grafo")
            continue
        
        graph.dfs_biggest_cost(starting_vertex, finishing_vertex, 0, [])
        print(f"O tamanho do maior caminho de {starting_vertex} a {finishing_vertex} é: {graph.max_cost}")
        print(f"O maior caminho de {starting_vertex} a {finishing_vertex} é: {graph.max_path}")
        break

app_thread = Thread(target=interact_with_map)
app_thread.start()

plt.subplot(121)
nx.draw(G, with_labels=True, font_weight="bold")
plt.show()

