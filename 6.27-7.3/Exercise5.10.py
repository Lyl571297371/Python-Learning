#coding:gb2312
#if��䴦���б�
requested_toppings=['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
	if requested_topping=="green peppers":
		print("Sorry,we are out of green peppers right now.")
	else:
		print("Please adding "+requested_topping +"!")
print("\nFinished making pizza.")


#�����б�Ϊ�գ������pizzaʲô������
requested_toppings=[ ]
if requested_toppings:
	for requested_topping in requested_toppings:
		print("Please adding "+requested_topping +"!")
else:
	print("Are you sure you want a plain pizza?")    #���б�ִ��else����飬���Ԫ�صĻ���ִ��if�����
