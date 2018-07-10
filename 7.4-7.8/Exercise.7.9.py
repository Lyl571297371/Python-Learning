#coding:gb2312
#while练习 
#习题1
print("习题1：")
sandwiche_orders = ['j','y','b']
finished_sandwiches = []
while sandwiche_orders:
	new_sandwiches = sandwiche_orders.pop()
	print(new_sandwiches+",I made yout tuna sandwich.")
	finished_sandwiches.append(new_sandwiches)
print("\n制作好的三明治：")
print(finished_sandwiches)

#习题2
print("\n\n习题2：")
sandwiche_orders = ['j','y','b','y','k','y','l']
print(sandwiche_orders)
print("抱歉，店里的y今天卖完了。")
while 'y' in sandwiche_orders:
	sandwiche_orders.remove('y')
print(sandwiche_orders)

#习题3
print("\n\n习题3：")
places = {}
active = True
while active:
	name = input("\nWhat's your name?  ")
	place = input("If you could visit one place,where would you go?  ")
	places[name] = place
	answer = input("Would you like to let another person respond？（Y/N）  ")
	if answer.upper() == 'N':
		active = False
print("\n\n***调查结果是***")
for name,place in places.items():
	print(name.title()+"最想去的地方是："+place+".")
