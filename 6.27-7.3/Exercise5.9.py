#coding:gb2312
#if语句练习题2

#if-elif-else
age=23
if age<2:
	print("他是婴儿")
elif 2<=age<4:
	print("他正蹒跚学步")
elif 4<=age<13:
	print("他是儿童")
elif 13<=age<20:
	print("他是青少年")
elif 20<=age<65:
	print("他是成年人")
else:
	print("他是老年人")


#if语句测试多个条件
fruits=['orange','apple','banana']
if 'apple' in fruits:
	print("Apple is my favorite fruit！")
if 'orange' in fruits:
	print("I really like oranges!")
if 'banana' in fruits:
	print("I really like bananas!")
if 'strawberry' not in fruits:
	print("Please buy some strawberries!")
