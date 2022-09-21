class Transport:
	def __init__(self, name, weight, price):
		self.name = name
		self.weight = weight
		self.price = price

	def getName(self):
		return self.name

	def getWeight(self):
		return self.weight

	def getPrice(self):
		return self.price

class Car(Transport):
	def __init__(self, name, weight, price, price_safe):
		Transport.__init__(self, name, weight, price)
		self.price_safe = price_safe

	def getPriceSafe(self):
		return self.price_safe


car = Car('Ferrari', 300.78, 3500.00, 800)

print(car.getName())
print(car.getWeight())
print(car.getPrice())
print(car.getPriceSafe())