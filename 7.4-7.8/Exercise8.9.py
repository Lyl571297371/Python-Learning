#coding:gb2312
#�����б�
def hello(names):
	for name in names:
		msg ="Hello,"+name.title()+"!"
		print(msg)
names=['lyl','cys','cby','cj']
hello(names)

#�ں������޸��б�
print("\n\n")
unprinted_numbers = ['2','3','4','5','6','7']
printed_numbers =[]
def print_numbers(unprinted_numbers,printed_numbers):
	while unprinted_numbers:
		new_num = unprinted_numbers.pop()
		print("���ڴ�ӡ�����֣� "+new_num)
		printed_numbers.append(new_num)
def show_printed_numbers(printed_numbers):
	print("��ӡ�õ����֣�")
	for num in printed_numbers:
		print(num)
print_numbers(unprinted_numbers[:],printed_numbers) #���ǰ����Ƭ������ʼ����
show_printed_numbers(printed_numbers)

