#coding:gb2312
#习题1
print("\n\n习题1：")
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
services=Restaurant('tianzi','chuancai')
services.describe_restaurant()
services.update_num_res(50)
#services.num_res()
services.incre_num_ser(20)
services.num_res()



#习题2
print("\n\n习题2:")
class User():
	def __init__(self,first_name,last_name,age,city):
		self.first_name=first_name
		self.last_name=last_name
		self.age=age
		self.city = city
		self.login_attempts=0
	def describe_user(self):
		print("The user's first name is "+self.first_name.title()+".")
		print("The user's last_name is "+self.last_name.title()+".")
		print("The user's age is "+str(self.age)+".")
		print("The user's city is "+self.city+".")
	def great_user(self):
		print("Hello,"+self.first_name.title()+' '+self.last_name.title()+"!\n\n")
	def read_login_attempts(self):
		print("这是该用户第 "+str(self.login_attempts)+" 次登录。")
	def incre_login_attempts(self):
		self.login_attempts += 1
	def reset_login_attempts(self):
		self.login_attempts = 0
a_user=User('liu','yanlong','23','yanan')
a_user.describe_user()
a_user.incre_login_attempts()
a_user.read_login_attempts()
a_user.incre_login_attempts()
a_user.read_login_attempts()
a_user.incre_login_attempts()
a_user.read_login_attempts()
a_user.incre_login_attempts()
a_user.read_login_attempts()
a_user.reset_login_attempts()
a_user.read_login_attempts()
