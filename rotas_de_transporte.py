from threading import Thread
from grafo import Graph

graph = Graph()
graph.read_csv("./grafo.csv")

print("Bem-vindo ao nosso sistema de rotas de transporte!")
print("-" * 24)

def interact_with_routes():
    while True:
        print("De onde e para onde você quer ir?")
        fron, to = input("Minha resposta (Ex.: A B): ").split(" ")
        if fron in graph.vertices and to in graph.vertices:
            break
        print("Resposta inválida. Um dos ou os dois caminhos não existem.")
    print("-" * 24)
    print("Calculando caminho...")
    print("-" * 24)
    jumps, path = graph.bfs_least_jumps(fron, to)
    print("Resultado:")
    print(f"Número de saltos: {jumps}")
    print(f"Caminho: {path}")

app_thread = Thread(target=interact_with_routes)
app_thread.start()

graph.draw_graph()
