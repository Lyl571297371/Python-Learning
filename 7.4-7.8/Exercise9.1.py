#coding:gb2312
#创建个使用雷类
class Dog():
	def __init__(self,name,age):
		self.name=name
		self.age =age
	def sit(self):
		print(self.name.title()+" is now sitting.")
	def roll_over(self):
		print(self.name.title()+" rolled over!")
my_dog = Dog('hurry','6')
print("My dog's name is "+my_dog.name.title()+".")
print("My dog is "+str(my_dog.age)+" years old "+".")
my_dog.sit()

your_dog =Dog('hali',9)
print("\n\nYour dog's name is "+your_dog.name.title()+".")
print("Your dog is "+str(your_dog.age)+" years old "+".")
your_dog.sit()
