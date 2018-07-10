#coding:gb2312
#结合使用函数和while循环
def name(first_name,last_name):
	full_name = first_name+' '+last_name
	return full_name.title()
while True:
	print("Please tell me your name: ") 
	print("(enter 'q' at any time to quit)")
	f_name=input("First_name:  ")
	if f_name == 'q':
		break
	l_name=input("Last_name:  ")
#	print("(enter 'q' at any time to quit)")
	if l_name == 'q':
		break
	friend=name(f_name,l_name)
	print("Hell,"+friend.title()+"\n\n")
