#coding:gb2312
#ϰ��1
print("\n\nϰ��1:")
def make_sandwiches (*toppings):
	print("�ù˿͵�������Ҫ�ӵ����У�")
	for topping in toppings:
		print("- "+topping)
make_sandwiches('s','d','v')
make_sandwiches('l')
make_sandwiches('q','w','e','r','t')

#ϰ��2
print("\n\nϰ��2:")
def build_profile(first,last,**info):
	profile={}
	profile['first_name']=first
	profile['last_name'] = last
	for key,value in info.items():
		profile[key]=value
	return profile
mes=build_profile('Liu','Yanlong',age='23',loc='Yanan',tel='000000')
print(mes)


#ϰ��3
print("\n\nϰ��3:")
def build_car_info(places,types,**other):
	file_0={}
	file_0['����']=places
	file_0['�ͺ�']=types
	for key,value in other.items():
		file_0[key]=value
	return file_0
file_1 = build_car_info('china','suv',date='2018',price='10w')
print(file_1)
	
