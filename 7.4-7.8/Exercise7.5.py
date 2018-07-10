#coding:gb2312
#使用标志
prompt = "\nTell me something,and i will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
active = True
while active:
	message = input(prompt)
	if message == 'quit':
		break                #任何python循环中都可以使用break语句退出循环，包括前面遍历列表和字典的for循环
	else:
		print(message)
		
#在循环中使用continue
num = 0
while num < 10:
	num += 1
	if num % 2 == 0:
		continue            #continue会让python忽略余下的代码，并返回到循环的开头
	print(num)
	
