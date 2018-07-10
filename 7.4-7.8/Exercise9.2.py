#coding:gb2312
#习题1
print("\n\n习题1:")
class Restaurant():
	def __init__(self,name,cuisine_type):
		self.name=name
		self.cuisine_type =cuisine_type
	def describe_restaurant(self):	
		print("The restaurant's name is "+self.name.title()+".")
		print("The restaurant's cuisine_type is "+self.cuisine_type.title()+".")
	def open_restaurant(self):
		print("The restaurant "+self.name.title()+" is opening.\n\n")
my_restaurant=Restaurant('xiaoyun','xiangcai')
lyl_restaurant=Restaurant('longteng','chuncai')
cys_restaurant=Restaurant('yijiabaoyan','yuecai')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
lyl_restaurant.describe_restaurant()
lyl_restaurant.open_restaurant()
cys_restaurant.describe_restaurant()
cys_restaurant.open_restaurant()

#习题2
print("\n\n习题2:")
class User():
	def __init__(self,first_name,last_name,age,city):
		self.first_name=first_name
		self.last_name=last_name
		self.age=age
		self.city = city
	def describe_user(self):
		print("The user's first name is "+self.first_name.title()+".")
		print("The user's last_name is "+self.last_name.title()+".")
		print("The user's age is "+str(self.age)+".")
		print("The user's city is "+self.city+".")
	def great_user(self):
		print("Hello,"+self.first_name.title()+' '+self.last_name.title()+"!\n\n")
a_user=User('liu','yanlong','23','yanan')
a_user.describe_user()
a_user.great_user()
b_user=User('chen','yisong','23','suzhou')
b_user.describe_user()
b_user.great_user()
