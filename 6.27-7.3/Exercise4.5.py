#coding:gb2312
#数字列表练习题2

#奇数
uneven_number=list(range(1,20,2))
print(uneven_number)
for number in uneven_number:
	print(number)

#3的倍数
number=[value*3 for value in range(1,10)]#3-30内能被3整除的数，不包含30
print(number)
for value in number:
	print(value)
	
#立方
numbers=[]
for value in range(1,10):
	number=value**3
	numbers.append(number)
print(numbers)
for value in numbers:
	print(value)
	
#立方解析
cubic_number=[value**3 for value in range(1,10)]#不包含10
print(cubic_number)
for value in cubic_number:
	print(value)
 
