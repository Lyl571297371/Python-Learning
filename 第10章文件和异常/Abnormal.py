#coding:gb2312
#ʹ��try-except����鴦������������쳣
print("Give me two numbers,and I'll divide them.")
print("Enter 'S' to quit.")
while True:
	first_num = input("Please enter first number:  ")
	if first_num.upper() == 'S':
		break
	second_num = input("Please enter second number:  ")
	try:
		answer = int(first_num)/int(second_num)
	except ZeroDivisionError:
		print("You can't divide by 0!\n\n")
	else:
		print(str(answer)+"\n\n")
