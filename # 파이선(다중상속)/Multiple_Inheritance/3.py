class Cal (object):
	def __init__(self,v1, v2):
		self.v1 = v1
		self.v2 = v2

	def add (self):
		return self.v1 + self.v2
	def subtract(self):
		return self.v1 - self.v2
	def setV1 (self, v):
		if isinstance (v, int) :
			self.v1 = v1
	def getV1 (self):
		return self.v1

class CalMultiply():
	def multiply(self):
		return self.v1 * self.v2

class CalDivide (Cal, CalMultiply):
	def divide (self):
		return self.v1 / self.v2

c1 = CalDivide (10, 10)
print(c1.multiply())
print(c1.add())
print(c1.subtract())
print(c1.divide())
