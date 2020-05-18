class Cs:
	count = 0
	def __init__ (self):
		Cs.count = Cs.count + 1

	@classmethod
	def getCount(cls):
		return cs.count

i1 = Cs()
i2 = Cs()
i3 = Cs()
print(Cs.getCount())
