import csv

class Node:
    def __init__(self, data: int|str, weight: int|None = None) -> None:
        self.data = data
        self.next = None
        self.weight = weight

    def __repr__(self):
        return self.data


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
        self.max_cost: int = -1
        self.max_path: list[Node] = []
        self.visited_dfs: list[str|int] = []

    def read_csv(self, filepath: str) -> None:
        with open(filepath, "r", newline='') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                fron, to = row["Origem"], row["Destino"]
                self.insert_vertex(fron)
                self.insert_vertex(to)
                self.insert_edge(fron, to, int(row["Peso"]))
    
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
    
    def reset_max_path_and_cost(self):
        self.max_cost = -1
        self.max_path = []
        self.visited_dfs = []

    def dfs_biggest_cost(
            self, 
            fron: int|str, 
            to: int|str, 
            current_cost: int, 
            current_path: list[int|str]
    ) -> None:
        if fron not in self.vertices or to not in self.vertices:
            raise Exception("Vertex doesn't exist in graph")

        self.visited_dfs.append(fron)
        if fron == to:
            if current_cost > self.max_cost:
                self.max_cost = current_cost
                self.max_path = current_path

        current = self.vertices[fron].head
        while current:
            if current.data not in self.visited_dfs:
                self.dfs_biggest_cost(
                    current.data,
                    to,
                    current_cost + current.weight,
                    current_path + [current]
                )
            current = current.next
        self.visited_dfs.remove(fron)

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
