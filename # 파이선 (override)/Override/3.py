class Cal (object):
	_history = []

	def __init__(self,v1, v2):
		self.v1 = v1
		self.v2 = v2

	def add (self):
		result = self.v1 + self.v2
		Cal._history.append("add : %d+%d=%d" %(self.v1, self.v2, result))
		return result

	def subtract(self):
		result = self.v1 - self.v2
		Cal._history.append("add : %d-%d=%d" %(self.v1, self.v2, result))
		return result

	def setV1 (self, v):
		if isinstance (v, int) :
			self.v1 = v1

	def getV1 (self):
		return self.v1

	@classmethod
	def history(cls):
		for item in Cal._history:
			print(item)
	def info(self):
		return "Cal v1 : %d, v2 : %d" % (self.v1, self.v2)

class CalMultiply(Cal):
	def multiply(self):
		result  = self.v1 *self.v2
		Cal._history.append("add : %d*%d=%d" %(self.v1, self.v2, result))
		return result

	def info(self):
		return "CalMultiply => %s" % super().info()

c0 = Cal(30, 60)
print (c0.info())
c1 = CalMultiply(10, 10)
print (c1.info())
