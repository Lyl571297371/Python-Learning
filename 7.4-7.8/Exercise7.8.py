#coding:gb2312
#ʹ���û�����������ֵ� 
print("ʹ���û�����������ֵ䣺")
favorite_numbers = {}
active = True
while active:
	name = input("\nWhat's your name?  ")
	numbers = input("What's your favorite number?  ")
#	numbers = int(numbers)
	favorite_numbers[name] = numbers
	answer = input("Would you like to let another person respond����Y/N��")
	if answer.upper() == 'N':
		active = False

print("\n\n***��������***")
for name,numbers in favorite_numbers.items():
	print(name.title()+"'s favorite number is "+str(numbers)+".")
