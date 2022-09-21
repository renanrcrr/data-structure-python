import random

class point:
	def __init__(self, id_point, values):
		self.id_point = id_point
		
		self.values = values
		
		self.total_values = len(values)
		
		self.id_cluster = -1

	def getID(self):
		return self.id_point

	def setCluster(self, id_cluster):
		self.id_cluster = id_cluster

	def getCluster(self):
		return self.id_cluster

	def getValue(self, index):
		return self.values[index]

	def getTotalValues(self):
		return self.total_values

	def addvalue(self, value):
		self.values.append(value)

class Cluster:
	def __init__(self, id_cluster, point):
		self.id_cluster = id_cluster
		
		self.total_values = point.getTotalValues()
		
		self.values_centrais = []
		
		self.points = []

		for i in range(self.total_values):
			self.values_centrais.append(point.getValue(i))

		self.points.append(point)

	def addPoint(self, point):
		self.points.append(point)

	def removePoint(self, id_point):
		total_points = len(self.points)
		
		for i in range(total_points):
			if self.points[i].getID() == id_point:
				self.points.pop(i)
				
				return True
		
		return False

	def getValueCentral(self, index):
		return self.values_centrais[index]

	def setvalueCentral(self, index, value):
		self.values_centrais[index] = value

	def getpoint(self, index):
		return self.points[index]

	def getTotalpoints(self):
		return len(self.points)

	def getID(self):
		return self.id_cluster

class KMeans:
	def __init__(self, K, total_points, total_values, max_iter):
		self.K = K
		
		self.total_points = total_points
		
		self.total_values = total_values
		
		self.max_iter = max_iter
		
		self.clusters = []

	def run(self, points):
		if self.K > self.total_points:
			print('Error: number of clusters is greater than number of points.')
			
			return

		prohibited_indexes = []

		for i in range(self.K):
			while True:
				index_point = random.randint(0, self.total_points - 1)
				
				if index_point not in prohibited_indexes:
					prohibited_indexes.append(index_point)
					
					self.points[index_point].setCluster(i)
					
					cluster = Cluster(i, self.points[index_point])
					
					self.clusters.append(cluster)
					
					break

		iter_ = 1

		while True:

			done = True

			for i in range(self.total_points):
				id_cluster_old = self.points[i].getCluster()
				
				id_cluster_proximo = getIDCentroProximo(self.points[i])

				if id_cluster_old != id_cluster_novo:
					if id_cluster_old != -1:
						self.clusters[id_cluster_old].removePoint(self.points[i].getID())
					
					self.points[i].setCluster(id_cluster_proximo)
					
					self.clusters[id_cluster_proximo].addPoint(self.points[i])
					
					done = False

			for i in range(self.K):
				for j in range(self.total_values):
					total_points_cluster = self.clusters[i].getTotalpoints()
			
					sums = 0.0

					if total_points_cluster > 0:
						for k in range(total_points_cluster):
							sums += self.clusters[i].getpoint(k).getValue(j)
						
						self.clusters[i].setvalueCentral(j, sums / total_points_cluster)

			if done == True or iter_ >= max_iter:
				print("Stopped at iteration %d" % iter_)
				
				break

			iter_+=1

		for i in range(self.K):
			print('\nCluster %d: ' % i, end='')
			
			for j in range(self.total_points_cluster):
				print('%d ' % self.clusters[i].getpoint(j).getID() + 1, end='')



if __name__ == "__main__":
	arq = open('dataset.txt')
	
	lines = arq.readlines()
	
	arq.close()
	
	first_line = lines[0].split()
	
	num_points, num_attributes, num_clusters, max_iter = [int(i) for i in first_line]

	points = []
	
	for i in range(1, num_points + 1):
		attributes = lines[i].split()
		
		points.append([float(i) for i in attributes])

	for point in points:
		print(point)