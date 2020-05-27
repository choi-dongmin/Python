class C1():
	def c1_m(self):
		print('c1')

class C2():
	def c2_m(self):
		print('c2')

class C3(C1, C2):
	pass

c = C3()
c.c1_m()
