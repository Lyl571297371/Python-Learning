#coding:gb2312
#��������������ʵ��  
def enter_number(*numbers):   #һ��*����һ����Ԫ�飬����*����һ�����ֵ�
	print("��������֣�")
	for num in numbers:
		print("- "+str(num))
enter_number('9')
enter_number('1','2','3','4')


#���ʹ��λ��ʵ�κ���������ʵ��
def make_pizza(size,*toppings):
	print("\n\nMaking a "+str(size)+"-inch pizza with the following toppings:")
	for top in toppings:
		print("- "+top.title())
make_pizza(12,'orange')
make_pizza(24,'pepperoni','mushrooms','green peppers')
