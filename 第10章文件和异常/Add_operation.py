#coding:gb2312
print("You can enter 's' at any time to quit.")
while True:
	try:
		num_1 = input("Give me a number: ")
		if num_1 == 's':            
			break
		num_1 = int(num_1)
		num_2 = input("Give me another number: ")
		if num_2 == 's':
			break
		num_2 = int(num_2)
	except ValueError:
		print("Sorry, I really needed a number.\n\n")
	else:
		sum = num_1 + num_2
		print("The sum of " + str(num_1) + " and " + str(num_2) + " is " + str(num_1+num_2) + ".\n\n")
