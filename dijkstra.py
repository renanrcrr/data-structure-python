from collections import defaultdict
import heapq

class MinHeap:
	def __init__(self):
		self._queue = []
		
		self._index = 0

	def insert(self, item, priority):
		heapq.heappush(self._queue, (-priority, self._index, item))
		
		self._index += 1

	def remove(self):
		return heapq.heappop(self._queue)[-1]

	def get_length(self):
		return len(self._queue)

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)
		
		self.vertexes = {}

	def addEdge(self, src, dest, cost):
		self.graph[src].append((dest, cost))
		
		self.vertexes[src] = src
		
		self.vertexes[dest] = dest

	def dijkstra(self, src, dest):
		number_vertexes = len(self.vertexes)

		p = [None for i in range(number_vertexes)]

		p[src] = 0

		min_heap = MinHeap()

		min_heap.insert(src, 0)

		while min_heap.get_length() > 0:
			u = min_heap.remove()

			for edge in self.graph[u]:
				v, cost = edge

				if p[v] is None or p[v] > p[u] + cost:
					p[v] = p[u] + cost

					min_heap.insert(v, p[v])

		return p[dest]

g = Graph()

g.addEdge(0, 1, 1)
g.addEdge(0, 3, 3)
g.addEdge(0, 4, 10)
g.addEdge(1, 2, 5)
g.addEdge(2, 4, 1)
g.addEdge(3, 2, 2)
g.addEdge(3, 4, 6)

print(g.dijkstra(0, 4))