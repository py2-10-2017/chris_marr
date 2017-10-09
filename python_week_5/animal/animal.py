class Animal(object):
	"""docstring for Animal"""
	def __init__(self, name, health):
		self.name = name
		self.health = health

	def walk(self):
		self.health -=1
		return self
		
	def run(self):
		self.health -=5
		return self

	def display_health(self):
		print "{}'s health is {}".format(self.name, self.health)
		return self

fluffy = Animal("Fluffy", 0)
fluffy.walk().walk().walk().run().run()
fluffy.display_health()

class Dog(Animal):
	"""docstring for Dog"""
	def pet(self):
		self.health += 5
		return self
		
snuffles = Dog("Snuffles", 150)
snuffles.walk().walk().walk().run().run()
snuffles.display_health()