class Graph:
	def __init__(self, vertices):
		self.vertices = vertices
		
		self.graph = [[0] * vertices for i in range(vertices)]

	def add_edge(self, u, v):
		self.graph[u - 1][v - 1] = 1
		
		self.graph[v - 1][u - 1] = 1

	def show(self):
		for i in self.graph:
		
			for j in i:
				print(j, end=' ')
				
			print('')

	def has_link(self, u, v):
		if self.graph[u - 1][v - 1] == 1:
			return True
		
		return False

	def bfs(self, v):
		visitados = [False] * self.vertices
		
		visitados[v - 1] = True
		
		queue = [v - 1]

		print('%d visited' % v)

		while len(queue) > 0:
			v = queue[0]

			for u in range(self.vertices):
				if self.graph[v][u] == 1:
					
					if visitados[u] == False:
						visitados[u] = True
						
						queue.append(u)
						
						print('%d visited' % (u + 1))

			queue.pop(0)

g = graph(10)

g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(3, 6)
g.add_edge(3, 7)
g.add_edge(4, 8)
g.add_edge(5, 9)
g.add_edge(6, 10)

g.bfs(1)