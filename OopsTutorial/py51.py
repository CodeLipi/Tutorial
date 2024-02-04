class Test:
	def __init__(self,name,id):
		self.name = name
		self.id = id
	def __str__(self):
		return 'name : {},id : {}'.format(self.name,self.id)
		

t = Test('kush','id')
print(t)