#coding:gb2312 
#ϰ��1
print("ϰ��1:")
names=['lyl','cys','cby']
def show_magicans(names):
	for name in names:
		print(name)
show_magicans(names)
 
#ϰ��2
print("\n\nϰ��2:")
names=['lyl','cys','cby']
great=[]
def show_magicans(names):
	while names:
		new_name = names.pop()
		print("ħ��ʦ�б� "+new_name)
		great.append("the great "+new_name.title())
		
def make_great(great):
	print("ΰ���ħ��ʦ��")
	for name in great:
		print(name.title()+"!")
show_magicans(names[:])
make_great(great)
print(names)
print(great)
