#coding:gb2312
#ϰ��1
filename = 'guest.txt'
print("Please enter 's' to quit.")
while True:
	name = input("What's your name? ")
	if name.lower() == 's':
		break
	else:
		with open(filename,'a') as f:
			f.write(name+"\n")
