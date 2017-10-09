class Car(object):
	"""docstring for Car"""
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		if (price > 10000):
			self.tax = "0.15"
		else:
			self.tax = "0.12"
		self.display_all()

	def display_all(self):
		print "The car's price is {}, the maximum speed is {}, the fuel gauge reads {}, the mileage is {}, and the tax is {}.".format(self.price, self.speed, self.fuel, self.mileage, self.tax)
		
car1 = Car("$2000", "35mph", "Full", "15mpg")
car2 = Car("$2000", "5mph", "Not Full", "105mpg")
car3 = Car("$2000", "15mph", "Kind of Full", "95mpg")
car4 = Car("$2000", "25mph", "Full", "25mpg")
car5 = Car("$2000", "45mph", "Empty", "25mpg")
car6 = Car("$2000000", "35mph", "Empty", "15mpg")

