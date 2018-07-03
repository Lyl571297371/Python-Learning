#coding:gb2312
#if语句处理多个列表
available_toppings=['mushrooms','olives','green peppers','pepperoni','pineapple','extra chees']
requested_toppings=['pineapple','mushrooms','french fries']
for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding "+requested_topping+'.')
	else:
		print("Soory,we don't have "+requested_topping+'.')
print("\nFinished making your pizza!")
