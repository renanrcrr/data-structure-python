class Person:
	def __init__(self, name, prior):
		self.name = name
		self.prior = prior

	def getName(self):
		return self.name

	def getPrior(self):
		return self.prior

class PriorityQueue:
	def __init__(self):
		self.pq = [] 
		self.len = 0 

	def push(self, person):
		if self.empty():
			self.pq.append(person)
		else:

			flag_push = False

			for i in range(self.len):
				if self.pq[i].getPrior() < person.getPrior():
					self.pq.insert(i, person)
					flag_push = True
					break

			if not flag_push:
				self.pq.insert(self.len, person)

		self.len += 1

	def pop(self):
		if not self.empty():
			self.pq.pop(0)
			self.len -= 1

	def empty(self):
		if self.len == 0:
			return True
		return False

	def show(self):
		for p in self.pq:
			print('Name: %s' % p.getName())
			print('Priority: %d\n' % p.getPrior())

p1 = Person('Mike', 21)
p2 = Person('Mika', 11)
p3 = Person('Mafalda', 22)
p4 = Person('Maye', 30)

pq = PriorityQueue()

pq.push(p1)
pq.push(p2)
pq.push(p3)
pq.push(p4)

print('Showing after inserts:\n')

pq.show() 
pq.pop()
pq.pop()

print('Showing after removals:\n')

pq.show() 
pq.push(Person('Goku', 30))

print('Showing after a insert:\n')

pq.show() 