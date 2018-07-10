#coding:gb2312
#input()和int()练习题
#习题1
print("习题1：")
message="Welcome to our car rental commpany!"
message+="\nWhat kind of car would you like to rent?"
mes=input(message)
print("Let me see if i can find you a "+mes+"!")


#习题2
print("\n\n习题2：")
number = input("How many peoples do you have?")
number = int(number)
if number>8:
	print("Sorry,we don't have enough tables!")
else:
	print("Ok,we have enough tables!")
	

#习题3
print("\n\n习题3：")
message="Please entet a number, and we will tell you if it's an integer multiple of 10"
message+="\nEnter number:"
mes=input(message)
mes=int(mes)
if mes%10==0:
	print("The number "+str(mes)+" is an integer multiple of 10.")
else:
	print("The number "+str(mes)+" is not an integer multiple of 10.")
