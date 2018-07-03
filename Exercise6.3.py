#coding:gb2312
#字典的学习2
#遍历字典，遍历字典的所有键和所有值
numbers=[6,9,8]
favorite_numbers={
	'lyl':1,
	'hl':6,
	'cby':9,
	'cys':2,
	'ft':3,
	}
#for name,number in favorite_numbers.items():  #声明两个变量用于遍历字典的for循环
#	print(name.title()+"'s favorite number is "+str(number)+".\n\n")
print("列表中包含的姓名：")
for name in sorted(favorite_numbers.keys()):  #sorted()将字母正序排序
	print(name.title())
print("列表中包含的数字：")
for number in favorite_numbers.values():
	print(str(number))
	if number not in numbers:
		print(str(number)+"is not in numbers"+".")
		
		
