#coding:gb2312
#ʹ�����ʵ��
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
	
	def update_odometer(self,mileage):       #�޸�����ֵ����2��ͨ�������޸����Ե�ֵ
		if mileage>=self.odometer_reading:
			self.odometer_reading=mileage
		else:
			print("You can't roll bcak an odometer!")
	def increment_odometer(self,miles):
		self.odometer_reading =self.odometer_reading+ miles		
my_car=Car('2018','audi','a4')
print(my_car.describe_car())
#my_car.odometer_reading=20      #�޸�����ֵ����1��ʹ�þ���ʾ��ֱ�ӷ��ʲ���������������odometer
my_car.update_odometer(50)
my_car.read_odometer()
my_car.increment_odometer(100)
my_car.read_odometer()

