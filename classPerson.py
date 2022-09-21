class Person:
	def __init__(self):
		self.__name = None

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, name):
		self.__nome = name

p = Person()

p.name = 'Renan'

print(p.name)