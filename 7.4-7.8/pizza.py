#coding:gb2312
#Ϊѧϰ�������洢��ģ����������

def make_pizza(size,*toppings):
	print("\n\nMaking a "+str(size)+"-inch pizza with following toppings:")
	for topping in toppings:
		print("- "+topping)
