#coding:gb2312
#习题1
print("\n\n习题1:")
def make_sandwiches (*toppings):
	print("该顾客的三明治要加的料有：")
	for topping in toppings:
		print("- "+topping)
make_sandwiches('s','d','v')
make_sandwiches('l')
make_sandwiches('q','w','e','r','t')

#习题2
print("\n\n习题2:")
def build_profile(first,last,**info):
	profile={}
	profile['first_name']=first
	profile['last_name'] = last
	for key,value in info.items():
		profile[key]=value
	return profile
mes=build_profile('Liu','Yanlong',age='23',loc='Yanan',tel='000000')
print(mes)


#习题3
print("\n\n习题3:")
def build_car_info(places,types,**other):
	file_0={}
	file_0['产地']=places
	file_0['型号']=types
	for key,value in other.items():
		file_0[key]=value
	return file_0
file_1 = build_car_info('china','suv',date='2018',price='10w')
print(file_1)
	
