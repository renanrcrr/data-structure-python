import operator

class Person:

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def getName(self):
		return self.name

	def getAge(self):
		return self.age

p1 = Person('Marcos', 28)
p2 = Person('Pedro', 20)
p3 = Person('Carol', 30)
p4 = Person('Yankee', 25)

people = [p1, p2, p3, p4]

people.sort(key=operator.attrgetter('age'), reverse=True)

for person in people:
	print('Name: %s, age: %d' % (person.getName(), person.getAge()))