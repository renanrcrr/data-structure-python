import random

class GeneratorGraph:
	def __init__(self, n):
		self.n = n
		
		self.graph = [[] for i in range(n)]
		
		self.costs = {}


	def produce_graph(self):
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
			print('Adjacent to %d:' % i, end=' ')
			for adj in self.graph[i]:
				print('(Cost %d) -> %d ->' % (self.costs[i, adj], adj), end=' ')
			print('')


	def pcv_random(self, iteracoes):

		best_circuit = []
		melhor_cost = None

		def produce_circuit(best_circuit, melhor_cost):

			vertices = [i for i in range(1, self.n)]
			circuit = [0]
			cost_circuit = 0

			while len(vertices) > 0:
				e = random.choice(vertices)
				vertices.remove(e)
				cost_circuit += self.costs[(circuit[-1], e)]
				circuit.append(e)

			cost_circuit += self.costs[(circuit[-1], 0)]

			if melhor_cost is None:
				best_circuit = circuit[:]
				melhor_cost = cost_circuit
			else:
				if cost_circuit < melhor_cost:
					best_circuit = circuit[:]
					
					melhor_cost = cost_circuit

			return (best_circuit, melhor_cost)

		for i in range(iteracoes):
			best_circuit, melhor_cost = produce_circuit(best_circuit, melhor_cost)

		print('Melhor circuit: %s\ncost: %d' % (str(best_circuit), melhor_cost))
			

	def pcv_genetico(self, tam_pop, generations, tam_tournament, prob_cruz, prob_mut):
		pop = [] 

		def produce_individuo():
			vertices = [i for i in range(1, self.n)]
			
			individuo = [0]
			
			while len(vertices) > 0:
				e = random.choice(vertices)
				
				vertices.remove(e)
				
				individuo.append(e)
			
			return individuo

		def obter_cost(individuo):
			cost = 0
			
			for i in range(self.n - 1):
				cost += self.costs[(individuo[i], individuo[i + 1])]
			
			cost += self.costs[(individuo[-1], individuo[0])]
			
			return cost

		for i in range(tam_pop):
			pop.append(produce_individuo())

		for i in range(generations):
			for j in range(tam_tournament):
				if random.random() <= prob_cruz:
					pai1, pai2 = None, None

					while True:
						pai1 = random.randint(0, tam_pop - 1)
						
						pai2 = random.randint(0, tam_pop - 1)
			
						if pai1 != pai2:
							break

					gen1_valid = [i for i in range(self.n)]
					
					gen2_valid = gen1_valid[:]
					
					son1, son2 = [], []

					while True:						
						ponto = random.randint(0, self.n - 1)

						if ponto != 0 and ponto != (self.n - 1):
							for p in range(ponto):
								if pop[pai1][p] not in son1:
									son1.append(pop[pai1][p])
									
									gen1_valid.remove(pop[pai1][p])
								
								else:
									e = random.choice(gen1_valid)
									
									son1.append(e)
									
									gen1_valid.remove(e)

								if pop[pai2][p] not in son2:
									son2.append(pop[pai2][p])
									
									gen2_valid.remove(pop[pai2][p])
								
								else:
									e = random.choice(gen2_valid)
									
									son2.append(e)
									
									gen2_valid.remove(e)

							for p in range(ponto, self.n):
								if pop[pai2][p] not in son1:
									son1.append(pop[pai2][p])
									
									gen1_valid.remove(pop[pai2][p])
								
								else:
									e = random.choice(gen1_valid)
									
									son1.append(e)
									
									gen1_valid.remove(e)

								if pop[pai1][p] not in son2:
									son2.append(pop[pai1][p])
									
									gen2_valid.remove(pop[pai1][p])
								
								else:
									e = random.choice(gen2_valid)
									
									son2.append(e)
									
									gen2_valid.remove(e)

							break

					if random.random() <= prob_mut:
						gene1, gene2 = None, None
						
						while True:
							gene1 = random.randint(0, self.n - 1)
							
							gene2 = random.randint(0, self.n - 1)
							
							if gene1 != gene2:
								son1[gene1], son1[gene2] = son1[gene2], son1[gene1]
								
								son2[gene1], son2[gene2] = son2[gene2], son2[gene1]
								
								break

					fitness_pai1 = obter_cost(pop[pai1])
					fitness_pai2 = obter_cost(pop[pai2])
					fitness_son1 = obter_cost(son1)
					fitness_son2 = obter_cost(son2)

					if fitness_son1 < fitness_pai1 or fitness_son1 < fitness_pai2:
						if fitness_son1 < fitness_pai1:
							pop.pop(pai1)
						
						else:
							pop.pop(pai2)
						
						pop.append(son1)
					
					elif fitness_son2 < fitness_pai1 or fitness_son2 < fitness_pai2:
						if fitness_son2 < fitness_pai1:
							pop.pop(pai1)
						
						else:
							pop.pop(pai2)
						
						pop.append(son2)

		best_individual = pop[0][:]
		
		for ind in range(1, tam_pop):
			if obter_cost(pop[ind]) < obter_cost(best_individual):
				best_individual = pop[ind][:]

		print('Best circuit: %s\ncost: %d' % (str(best_individual), obter_cost(best_individual)))


graph = Geradorgraph(50)
graph.produce_graph()

print('Random')
graph.pcv_random(1000)

print('\nGenetic Algorithm')
graph.pcv_genetico(tam_pop=2000, generations=1000, tam_tournament=1, prob_cruz=0.7, prob_mut=0.1)