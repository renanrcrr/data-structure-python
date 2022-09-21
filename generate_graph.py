import random

class GenerateGraph:
	def __init__(self, n):
		self.n = n
		
		self.graph = [[] for i in range(n)]
		
		self.costs = {}

	def create_graph(self):
		for i in range(self.n):
		
			for j in range(self.n):
				
				if i != j:
					if (i, j) and (j, i) not in self.costs:
						cost = random.randint(1, 100)
						
						self.costs[(i, j)] = cost
						
						self.costs[(j, i)] = cost
						
					self.graph[i].append(j)

	def show_graph(self):
		for i in range(self.n):
			print('Adjacentes de %d:' % i, end=' ')
			
			for adj in self.graph[i]:
				print('(cost %d) -> %d ->' % (self.costs[i, adj], adj), end=' ')
			
			print('')

	def pcv_random(self, iterations):
		best_circuit = []
		
		best_cost = None

		def create_circuit(best_circuit, best_cost):
			vertices = [i for i in range(1, self.n)]
			
			circuit = [0]
			
			cost_circuit = 0

			while len(vertices) > 0:
				e = random.choice(vertices)
				
				vertices.remove(e)
				
				cost_circuit += self.costs[(circuit[-1], e)]
				
				circuit.append(e)

			cost_circuit += self.costs[(circuit[-1], 0)]

			if best_cost is None:
				best_circuit = circuit[:]
				
				best_cost = cost_circuit
				
				print('circuit inicial: %s - cost: %d' % (str(best_circuit), best_cost))
			
			else:
				if cost_circuit < best_cost:
					best_circuit = circuit[:]
					
					best_cost = cost_circuit

			return (best_circuit, best_cost)

		for i in range(iterations):
			best_circuit, best_cost = create_circuit(best_circuit, best_cost)
			
			#print('Iter %d: Best circuit: %s - cost: %d' % (i + 1, str(best_circuit), best_cost))

		print('Best circuit: %s - cost: %d' % (str(best_circuit), best_cost))

gerador = GenerateGraph(10)

gerador.create_graph()

gerador.pcv_random(1000)