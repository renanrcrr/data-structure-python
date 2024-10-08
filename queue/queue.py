class Queue:
	def __init__(self):
		self.queue = []
		self.len_queue = 0

	def push(self, e):
		self.queue.append(e)
		self.len_queue += 1

	def pop(self):
		if not self.empty():
			self.queue.pop(0)
			self.len_queue -= 1

	def empty(self):
		if self.len_queue == 0:
			return True
		return False

	def length(self):
		return self.len_queue

	def front(self):
		if not self.empty():
			return self.queue[0]
		return None

	def __str__(self):
		return f'Current queue => {self.queue}'
	
q = Queue()
print(q)
q.push(1)
q.push(2)
q.push(3)
q.push(4)
print(q)
print(q.front())
q.pop()
print(q)