#coding:gb2312
#�̳�
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


class Ele_car(Car):      #�������������ָ�����������
	def __init__(self,year,make,module):      #���ܴ���Carʵ���������Ϣ
		super().__init__(year,make,module)    #����python����������������������python����Ele_car����ķ���__init__()����Ele_carʵ�������������������
		self.battery_size = 70
	
	def describe_battery(self):
		print("This car has a "+str(self.battery_size)+"-kwh battery.")

m_car=Ele_car('2018','byd','song')     
print(m_car.describe_car())
m_car.describe_battery()
