#coding:gb2312
#使用用户输入来填充字典 
print("使用用户输入来填充字典：")
favorite_numbers = {}
active = True
while active:
	name = input("\nWhat's your name?  ")
	numbers = input("What's your favorite number?  ")
#	numbers = int(numbers)
	favorite_numbers[name] = numbers
	answer = input("Would you like to let another person respond？（Y/N）")
	if answer.upper() == 'N':
		active = False

print("\n\n***调查结果是***")
for name,numbers in favorite_numbers.items():
	print(name.title()+"'s favorite number is "+str(numbers)+".")
