class Animal(object):
	"""docstring for Animal"""
	def __init__(self, name):
		self.name = name
		self.health = 0

	def walk(self):
		self.health -= 1
		return self
		
	def run(self):
		self.health -= 5
		return self

	def display_health(self):
		print "{}'s health is {}".format(self.name, self.health)
		return self

fluffy = Animal("Fluffy")
fluffy.walk().walk().walk().run().run()
fluffy.display_health()

class Dog(Animal):
	"""docstring for Dog"""
	def set_health(self):
		self.health = 150
		return self

	def pet(self):
		self.health += 5
		return self
		
snuffles = Dog("Snuffles")
snuffles.set_health().walk().walk().walk().run().run().pet()
snuffles.display_health()

class Dragon(Animal):
	def default_health(self):
		self.health = 170
		return self

	def fly(self):
		self.health -=10
		return self

	def display(self):
		print "I am a dragon."
		print self.display_health()

flame_eater = Dragon("Flame Eater")
flame_eater.default_health().fly().fly()
flame_eater.display()
