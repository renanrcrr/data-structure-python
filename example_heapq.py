import heapq

class Person:

	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return self.name

class queueOfPriority:

	def __init__(self):
		self._queue = []
		self._index = 0

	def insert(self, item, prioridade):
		heapq.heappush(self._queue, (-prioridade, self._index, item))
		self._index += 1

	def remove(self):
		return heapq.heappop(self._queue)[-1]


queue = queueOfPriority()

queue.insert(Person('Mariana'), 20)
queue.insert(Person('Maria'), 16)
queue.insert(Person('Marta'), 25)
queue.insert(Person('Mafalda'), 23)

print(queue.remove())