class C:
	def __init__(self, v):
		self.value = v

	def getValue (self):
		return self.value

	def setValue (self, v):
		self.value= v

c1 = C(10)
print(c1.getvalue())
c1.setValue(20)
print(getValue())
