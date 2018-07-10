#coding:gb2312
#习题2
filename = 'result.txt'
print("Please enter 'S' to quit!\n")
while True:
	answer = input("Why do you like programming?  ")
	if answer.upper() == 'S':
		break
	else:
		with open(filename,'a') as f:
			f.write(answer+"\n\n")
