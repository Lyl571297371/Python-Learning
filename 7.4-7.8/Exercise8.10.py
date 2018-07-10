#coding:gb2312 
#习题1
print("习题1:")
names=['lyl','cys','cby']
def show_magicans(names):
	for name in names:
		print(name)
show_magicans(names)
 
#习题2
print("\n\n习题2:")
names=['lyl','cys','cby']
great=[]
def show_magicans(names):
	while names:
		new_name = names.pop()
		print("魔术师列表： "+new_name)
		great.append("the great "+new_name.title())
		
def make_great(great):
	print("伟大的魔术师：")
	for name in great:
		print(name.title()+"!")
show_magicans(names[:])
make_great(great)
print(names)
print(great)
