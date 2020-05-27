class C1():
	def c1_m(self):
		print('c1')

	def m(self):
		print('c1_m')

class C2():
	def c2_m(self):
		print('c2')

	def m(self):
		print('c2_m')
class C3(C1, C2):
	pass

c = C3()
c.c1_m()
c.c2_m()
c.m()
