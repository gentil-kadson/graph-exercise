import csv

class Node:
    def __init__(self, data: int|str, weight: int|None = None) -> None:
        self.data = data
        self.next = None
        self.weight = weight
        self.visited = False


class LinkedList:
    def __init__(self, head: Node|None = None) -> None:
        self.head = head
    
    def append(self, data: int|str, weight: int) -> None:
        new_node = Node(data, weight)

        if self.head is None:
            self.head = new_node
            return
        
        last = self.head

        while last.next:
            last = last.next
        
        last.next = new_node
    
    def has(self, data: int|str) -> bool:
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def print(self) -> None:
        current = self.head
        while current:
            print(f"{current.data} ({current.weight})", end=" ")
            current = current.next
        print()
    
    def get_connected_vertices(self) -> list[int|str]:
        vertices = []
        current = self.head
        while current:
            vertices.append(current.data)
            current = current.next
        return vertices
    

class Graph:
    def __init__(self) -> None:
        self.vertices: dict[int|str, LinkedList] = {}
        self.max_cost: int = 0
        self.max_path: list[Node] = []
    
    def insert_vertex(self, vertex: int|str) -> None:
        if vertex in self.vertices:
            print("Esse vértice já está no grafo.")
            return
        self.vertices[vertex] = LinkedList()
    
    def insert_edge(self, vertexA: int|str, vertexB: int|str, weight: int) -> None:
        if vertexA not in self.vertices or vertexB not in self.vertices:
            print("Um dos vértices informados não existe.")
            return
        if self.vertices[vertexA].has(vertexB) and self.vertices[vertexB].has(vertexA):
            print("Estes vértices já estão conectados.")
            return
        self.vertices[vertexA].append(vertexB, weight)
        self.vertices[vertexB].append(vertexA, weight)
    
    def print(self) -> None:
        for vertex in self.vertices:
            print(f"Vizinhos do vértice {vertex}:")
            curr_vertex = self.vertices[vertex]
            if not curr_vertex.head:
                print("Não tem vizinhos.")
                continue
            curr_vertex.print()

    def dfs_biggest_cost(
            self, 
            fron: int|str, 
            to: int|str, 
            current_cost: int, 
            current_path: list[Node]
    ) -> None:
        if fron not in self.vertices:
            raise Exception("Vertex doesn't exist in graph")

        from_vertex: Node = self.vertices[fron]
        from_vertex.visited = True
        if fron == to:
            if current_cost > self.max_cost:
                self.max_cost = current_cost
                self.max_path = current_path
            from_vertex.visited = False
            return
        
        current = self.vertices[fron].head
        while current.next:
            adjacent_vertex: Node = current.next
            if not adjacent_vertex.visited:
                self.dfs_biggest_cost(
                    adjacent_vertex.data, 
                    to, 
                    current_cost + adjacent_vertex.weight,
                    current_path + [adjacent_vertex]
                )
        from_vertex.visited = False

    def bfs_least_jumps(self, fron: int | str, to: int | str) -> int | str:
        queue: list[tuple[int | str, int]] = []
        visited_vertices: list[int | str] = []

        queue.append((fron, 0))
        visited_vertices.append(fron)

        while len(queue) > 0:
            curr_vertex, jumps = queue.pop(0)
            if curr_vertex == to:
                return jumps
            for connected_vertex in self.vertices[curr_vertex].get_connected_vertices():
                if connected_vertex not in visited_vertices:
                    visited_vertices.append(connected_vertex)
                    queue.append((connected_vertex, jumps+1))
        return "Nenhum caminho encontrado"
    
graph = Graph()

with open("grafo.csv", "r", newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        fron, to = row["Origem"], row["Destino"]
        graph.insert_vertex(fron)
        graph.insert_vertex(to)
        graph.insert_edge(fron, to, int(row["Peso"]))

graph.print()

jumps = graph.bfs_least_jumps("D", "A")
print("-" * 24)
print(f"Resultado: {jumps} salto(s).")