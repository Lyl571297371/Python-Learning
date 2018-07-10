#coding:gb2312
#传递列表
def hello(names):
	for name in names:
		msg ="Hello,"+name.title()+"!"
		print(msg)
names=['lyl','cys','cby','cj']
hello(names)

#在函数中修改列表
print("\n\n")
unprinted_numbers = ['2','3','4','5','6','7']
printed_numbers =[]
def print_numbers(unprinted_numbers,printed_numbers):
	while unprinted_numbers:
		new_num = unprinted_numbers.pop()
		print("正在打印的数字： "+new_num)
		printed_numbers.append(new_num)
def show_printed_numbers(printed_numbers):
	print("打印好的数字：")
	for num in printed_numbers:
		print(num)
print_numbers(unprinted_numbers[:],printed_numbers) #结合前面切片保留初始数据
show_printed_numbers(printed_numbers)

