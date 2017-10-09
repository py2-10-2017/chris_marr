class Bike(object):
	"""docstring for Bike"""
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0

	def displayinfo(self):
		print "The bike's price is {}, the maximum speed is {}, and the total mileage is {}.".format(self.price, self.max_speed, self.miles)
		return self

	def ride(self):
		print "Riding."
		self.miles +=10
		return self

	def reverse(self):
		print "Reversing."
		self.miles -=5
		return self

bike1 = Bike("$100", "25mph")
bike2 = Bike("$20", "1mph")
bike3 = Bike("$500", "45mph")

bike1.ride().ride().ride().reverse().displayinfo()
bike2.ride().ride().reverse().reverse().displayinfo()
bike3.reverse().reverse().reverse().displayinfo()