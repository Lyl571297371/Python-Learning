#coding:gb2312
#传递任意数量的实参  
def enter_number(*numbers):   #一个*创建一个空元组，两个*创建一个空字典
	print("输入的数字：")
	for num in numbers:
		print("- "+str(num))
enter_number('9')
enter_number('1','2','3','4')


#结合使用位置实参和任意数量实参
def make_pizza(size,*toppings):
	print("\n\nMaking a "+str(size)+"-inch pizza with the following toppings:")
	for top in toppings:
		print("- "+top.title())
make_pizza(12,'orange')
make_pizza(24,'pepperoni','mushrooms','green peppers')
