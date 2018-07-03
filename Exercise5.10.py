#coding:gb2312
#if语句处理列表
requested_toppings=['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
	if requested_topping=="green peppers":
		print("Sorry,we are out of green peppers right now.")
	else:
		print("Please adding "+requested_topping +"!")
print("\nFinished making pizza.")


#假设列表为空，即点的pizza什么都不加
requested_toppings=[ ]
if requested_toppings:
	for requested_topping in requested_toppings:
		print("Please adding "+requested_topping +"!")
else:
	print("Are you sure you want a plain pizza?")    #空列表执行else代码块，添加元素的话，执行if代码块
