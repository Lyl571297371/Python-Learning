#coding:gb2312
#用户输入和while循环学习

#input()函数
message = "If you tell us who you are ,we can personalize the message you see."
message += "\nWhat is your name?"   #+=运算符是因为此处创建了多行字符串
name=input(message)
print("\nHello "+name+"!")

#int()获取整数输入
age=input("How old are you?")
age=int(age)        #注释掉此行代码就会出错，原因是python无法将字符串和整数进行比较
if age>=18:
	print("You are old enouh to vote"+"!")
else:
	print("Sorry,you will be able to vote when you are a little older"+".")


