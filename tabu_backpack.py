import random

backpack = [[4,2], [5,2], [7,3], [9,4], [6,4]]
iteration, best_iteration = 0, 0 
best_solution = [] 
list_tabu = [] 
max_capacity = 23 
bt_max = 1 
max_neighbors = 5 

for i in range(5):
	bit = random.randint(0, 1)
	best_solution.append(bit)

def get_evaluation(solution, backpack, max_capacity):
	sum_weight, sum_benefit = 0, 0

	for i in range(len(solution)):
		sum_weight += solution[i] * backpack[i][0]
		sum_benefit += solution[i] * backpack[i][1]
	evaluation = sum_benefit * (1 - max(0, sum_weight - max_capacity))

	return evaluation

def get_weight(solution, backpack):
	weight = 0
	for i in range(len(solution)):
		weight += solution[i] * backpack[i][0]
	return weight

def produce_neighbors(best_solution, max_neighbors):
	neighbors, pos = [], 0
	
	for i in range(max_neighbors):
		neighbor = []
		
		for j in range(len(best_solution)):
			if j == pos:
				if best_solution[j] == 0:
					neighbor.append(1)
					
				else:
					neighbor.append(0)
			else:
				neighbor.append(best_solution[j])
		
		neighbors.append(neighbor)
		
		pos += 1
		
	return neighbors

def get_evaluation_neighbors(neighbors, backpack, max_capacity, max_neighbors):
	neighbors_evaluation = []
	for i in range(max_neighbors):
		neighbors_evaluation.append(get_evaluation(neighbors[i], backpack, max_capacity))
	return neighbors_evaluation

def get_bit_changed(best_solution, melhor_neighbor):
	for i in range(len(best_solution)):
		if best_solution[i] != melhor_neighbor[i]:
			return i

def get_neighbor_best_evaluation(neighbors_evaluation, list_tabu, best_solution, neighbors):
	maxima_evaluation = max(neighbors_evaluation)
	pos = 0
	bit_prohibited = -1

	if len(list_tabu) != 0:
		bit_prohibited = list_tabu[0]

	for i in range(len(neighbors_evaluation)):
		if neighbors_evaluation[i] == maxima_evaluation:
			pos = i
			break

	if bit_prohibited != -1:
		bit_pos = get_bit_changed(best_solution, neighbors[pos])

		if bit_pos == bit_prohibited:

			best_pos = 0

			for i in range(len(neighbors_evaluation)):
				if i != bit_pos:
					if neighbors_evaluation[i] > neighbors_evaluation[best_pos]:
						best_pos = i

			return best_pos

	return pos

print('Initial solution: {0}, Evaluation: {1}'.format(best_solution, 
			get_evaluation(best_solution, backpack, max_capacity)))

