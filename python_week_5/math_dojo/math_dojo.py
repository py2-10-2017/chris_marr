## PART I ##

class MathDojo(object):
	def __init__(self):
		self.result = 0

	def add(self, *args):
		for nums in args:
			self.result +=nums
			print self.result
		return self

	def subtract(self, *args):
		for nums in args:
			self.result -=nums
			print self.result
		return self

md = MathDojo()
md.add(2).add(2,5).subtract(3,2).result

