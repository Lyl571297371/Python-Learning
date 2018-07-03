#coding:gb2312
#数字列表练习题1

#数到20
for numbers in range(1,21):
	print(numbers)

#一百万
numbers=[value for value in range(1,1000001)]
print(numbers) 

#计算1-1000000的总和
print(min(numbers))#确定是从1开始的
print(max(numbers))#确定是以1000000结束的
print(sum(numbers))#求和1-1000000
 
