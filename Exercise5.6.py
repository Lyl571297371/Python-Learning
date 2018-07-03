#coding:gb2312
#if语句学习

#简单的if语句，执行两个操作中的一个
print("简单的if语句：\n")
age=18
if age>=18:          #if语句和for语句有点相像，都要冒号，下一行都要缩进
	print("You are old enough to vote!")   #上述if语句测试通过了，才会继续执行if语句后缩进的的代码行
	print("Have you registersd to vote yet?")


#if-else语句
print("\n\nif-else语句：\n")
age=17
if age>=18:
	print("You are old enough to vote!")
	print("Have you registersd to vote yet?")  #若上述的age>=18，即条件测试通过，便执行此块缩进代码行
else:
	print("Sorry ,you are too young to vote.")
	print("Please register as soon as you turn 18.")  #age=17，不能通过条件测试，所以执行else的缩进代码行


#if-elif-else结构，适用于检查超过两个的情形，遇到了一个通过的测试将会跳过余下的测试，例如根据年龄段收费的游乐场
print("\n\nif-elif-else结构：\n")
age=23
if age<4:
	print("your admission cost is $0.")   #4岁以下免费
elif age<18:                              
	print("your admission cost is $5.")   #4<=age<18收费$5
else :
	print("your admission cost is $10.")  #大于等于18收费$10
#换了满足三次情形的age值，与结果相符
#还是这个问题，不过对代码进行了简洁修改
print("\n\n修改后：\n")
age=12
if age<4:
	price=0
elif age<18:
	price=5
else:
	price=10
#print("Your admission cost is "+price+".")       ###第一次写法，结果报错，因为price的值，没有用str()将非字符串值转化为字符串值
print("Your admission cost is "+"$"+str(price)+".")
#练习使用多个elif代码块
print("\n\n多个elif代码块：\n")
age=65
if age<4:
	price=0
elif age<18:
	price=5
elif age>=65:
	price=0
else:
	price=10    
print("Your admission cost is "+"$"+str(price)+".")
#省略else代码块
print("\n\n省略else代码块：\n")
age=65                                     #改变了多次值都符合预期结果
if age<4:
	price=0
elif 4<=age<18:
	price=5
elif 18<=age<65:
	price=10
elif age>=65:
	price=0
   
print("Your admission cost is "+"$"+str(price)+".")

#总结：if-elif-else遇到一个通过的测试便结束，效率高；简单说就是只想执行一个代码块
      #如果想要运行多个代码块的话，就用一系列独立的if语句
     
