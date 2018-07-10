#coding:gb2312
#while练习题1
#习题1
print("习题1：")
mes = "What ingredients do you need?"
mes += "\nEnter the ingredients you want to add:  "
active = True
while active:
	message = input(mes)
	if message == 'quit':
		active = False
	else:
		print("\nWe'll add this ingredient to the pizza："+message+".\n\n\n")
		
		
#习题2
print("\n\n习题2：")
message = "How old are you?"
age = ""
active = True
while active:
	age = input(message)
	if age == 'quit':
#		active = False             #使用标志来控制循环结束的时机
		break                      #使用break语句在用户输入'quit'时退出循环
	elif int(age)<3:
		print("您是免费的.\n")
	elif 3<=int(age)<12:
		print("您的票价是10$.\n")
	elif int(age)>=12:
		print("您的票价是15$.\n")
	
	
#习题三
print("\n\n习题3：没完没了的循环用ctrl+c停止")
num = 1
while num<=5:
	print(num)  
#	num += 1     #取消此行代码注释便不会无解的运行下去
