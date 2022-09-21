class Graph:
	def __init__(self, V):
		self.V = V
		
		self.list = [[] for i in range(V)]

	def add_aresta(self, orig, dest):
		self.list[orig].append(dest)

	def dfs(self, v):

		stack, stack_rec = [], []
		visited = [False for i in range(self.V)]
		stack_rec = [False for i in range(self.V)]

		while True:

			found_neighbor = False

			if not visited[v]:
				stack.append(v)
				visited[v] = stack_rec[v] = True

			aux_adj = None

			for adj in self.list[v]:

				aux_adj = adj

				if stack_rec[adj]:
					return True
				
				elif not visited[adj]:
					found_neighbor = True
					break

			if not found_neighbor:
				stack_rec[stack[-1]] = False

				stack.pop() 

				if len(stack) == 0:
					break

				v = stack[-1]
			
			else:
				v = adj

		return False


	def has_cyclo(self):
		for i in range(self.V):
			if self.dfs(i):
				return True
				
		return False


g = Graph(3)

g.add_aresta(0, 1)
g.add_aresta(1, 2)
g.add_aresta(2, 0)

print(g.has_cyclo())