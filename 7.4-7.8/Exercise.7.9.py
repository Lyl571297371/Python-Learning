#coding:gb2312
#while��ϰ 
#ϰ��1
print("ϰ��1��")
sandwiche_orders = ['j','y','b']
finished_sandwiches = []
while sandwiche_orders:
	new_sandwiches = sandwiche_orders.pop()
	print(new_sandwiches+",I made yout tuna sandwich.")
	finished_sandwiches.append(new_sandwiches)
print("\n�����õ������Σ�")
print(finished_sandwiches)

#ϰ��2
print("\n\nϰ��2��")
sandwiche_orders = ['j','y','b','y','k','y','l']
print(sandwiche_orders)
print("��Ǹ�������y���������ˡ�")
while 'y' in sandwiche_orders:
	sandwiche_orders.remove('y')
print(sandwiche_orders)

#ϰ��3
print("\n\nϰ��3��")
places = {}
active = True
while active:
	name = input("\nWhat's your name?  ")
	place = input("If you could visit one place,where would you go?  ")
	places[name] = place
	answer = input("Would you like to let another person respond����Y/N��  ")
	if answer.upper() == 'N':
		active = False
print("\n\n***��������***")
for name,place in places.items():
	print(name.title()+"����ȥ�ĵط��ǣ�"+place+".")
