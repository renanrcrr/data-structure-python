from collections import defaultdict

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def getName(self):
		return self.name

	def getAge(self):
		return self.age

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self, p1, p2):
		self.graph[p1.getName()].append(p2)
		self.graph[p2.getName()].append(p1)

	def showFriends(self, person):
		for friend in self.graph[person.getName()]:
			print('%s' % friend.getName())

g = Graph()

p1 = Person('Osley', 20)
p2 = Person('Joaquim', 30)
p3 = Person('Diego', 18)
p4 = Person('Patrick', 25)
p5 = Person('Igor', 14)

g.addEdge(p1, p2)
g.addEdge(p1, p3)
g.addEdge(p2, p4)
g.addEdge(p4, p3)
g.addEdge(p3, p5)
g.addEdge(p5, p1)

g.showFriends(p5)

