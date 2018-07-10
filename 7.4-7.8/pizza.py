#coding:gb2312
#为学习将函数存储在模块中所创建

def make_pizza(size,*toppings):
	print("\n\nMaking a "+str(size)+"-inch pizza with following toppings:")
	for topping in toppings:
		print("- "+topping)
