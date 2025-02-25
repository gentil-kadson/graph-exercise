import csv
from grafo import Graph

graph = Graph()
with open("grafo.csv", "r", newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        fron, to = row["Origem"], row["Destino"]
        graph.insert_vertex(fron)
        graph.insert_vertex(to)
        graph.insert_edge(fron, to, int(row["Peso"]))

print("Bem-vindo ao nosso sistema de rotas de transporte!")
print("-" * 24)
while True:
    print("De onde e para onde você quer ir?")
    for vertex in graph.vertices:
        print(f"-> {vertex}")
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
