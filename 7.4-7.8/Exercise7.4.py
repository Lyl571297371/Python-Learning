#coding:gb2312
#while循环简介
print("Whlie 循环从1数到5：")
num = 1
while num <=5:
	print(num)
	num += 1
	
#让用户选择何时退出
prompt = "\nTell me something,and i will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
message = ''
while message !='quit':
	message=input(prompt)
	if message !='quit':
		print(message)
