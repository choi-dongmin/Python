class Cs:
	@staticmethod
	def static_method():
		print('staic method')

	@classmethod
	def clas_ method(cls):
		print('class method')

	def instance_method(self):
		print('instance method')

i = Cs()
Cs.static_method()
Cs.class_method()
i.instance_method()
