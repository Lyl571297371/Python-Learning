#coding:gb2312
#创建数值列表和对列表进行一些简单的操作
for numbers in range(1,6):#range(1,6)只包含1，2，3，4，5，没有6
	print(numbers)

#range创建数字列表：
numbers=list(range(1,6))#list()将数字转化成列表
print(numbers)

even_numbers=list(range(2,14,2))#range(x,y,z)x,y表示数字范围，z表示步长即数字间的距离
print(even_numbers)

#比较下列三种创建列表的方式
#第一种
squares=[]
for number in range(1,11): 
	square=number**2
	squares.append(square)
print(squares)

#第二种
squares=[]
for number in range(1,11):
	squares.append(number**2)
print(squares)
 
#第三种
squares=[number**2 for number in range(1,11)]#nuber**2是定义的表达式；for number in range(1,11)for循环是用于给表达式提供值
print(squares)

#对数字列表执行简单的统计计算
print(min(squares))#数字列表最小值
print(max(squares))#数字列表最大值
print(sum(squares))#数字列表元素求和
