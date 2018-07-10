#coding:gb2312
#习题
class Restaurant():
	def __init__(self,name,cuisine_type):
		self.name=name
		self.cuisine_type =cuisine_type
		self.number_served = 0
	def describe_restaurant(self):	
		print("The restaurant's name is "+self.name.title()+".")
		print("The restaurant's cuisine_type is "+self.cuisine_type.title()+".")
	def open_restaurant(self):
		print("The restaurant "+self.name.title()+" is opening.\n\n")
	def num_res(self):	
		print("The restaurant have served "+str(self.number_served)+" peoples.")
	def update_num_res(self,cou):
		self.number_served = cou
	def incre_num_ser(self,count):
		self.number_served +=count

class Icecream(Restaurant):
	def __init__(self,name,cuisine_type):
		super().__init__(name,cuisine_type)
		self.flavors = []
	
	def describe_icecream(self):
		for flavor in self.flavors:
			print("冰淇淋配料："+flavor.title()+".")

m_ice=Icecream('hjj','sda')
m_ice.describe_restaurant()
m_ice.flavors = ['orange','apple','strawberry']
m_ice.describe_icecream()
