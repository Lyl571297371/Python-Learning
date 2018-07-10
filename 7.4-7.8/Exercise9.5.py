#coding:gb2312
#继承
class Car():
	def __init__ (self,year,make,module):
		self.year=year
		self.make=make
		self.module=module
		self.odometer_reading=23
	
	def describe_car(self):
		infomation=str(self.year)+' '+self.make.title()+' '+self.module.title()+'.'
		return infomation
	
	def read_odometer(self):
		print("This car has "+str(self.odometer_reading)+" miles on it.")
	
	def update_odometer(self,mileage):        
		if mileage>=self.odometer_reading:
			self.odometer_reading=mileage
		else:
			print("You can't roll bcak an odometer!")
	
	def increment_odometer(self,miles):
		self.odometer_reading =self.odometer_reading+ miles	


class Ele_car(Car):      #在子类的括号内指定父类的名称
	def __init__(self,year,make,module):      #接受创建Car实例所需的信息
		super().__init__(year,make,module)    #帮助python将父类和子类关联起来，让python调用Ele_car父类的方法__init__()，让Ele_car实例包含父类的所有属性
		self.battery_size = 70
	
	def describe_battery(self):
		print("This car has a "+str(self.battery_size)+"-kwh battery.")

m_car=Ele_car('2018','byd','song')     
print(m_car.describe_car())
m_car.describe_battery()
