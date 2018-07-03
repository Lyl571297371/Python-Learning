#coding:gb2312
#if语句处理列表练习题
#习题3 
print("习题3:")
current_users = ['lyl','cby','ft','fjy','cxk']
new_users = ['cys','lj','LYL','lf','fjy']
for new_user in new_users:
	if new_user.lower() in current_users:   #确保比较时不区分大小写
		print("此用户名已被使用： "+new_user)
	else:
		print("此用户名可以使用： "+new_user)
		
#习题4
print("\n\n习题4：")
numbers=list(range(1,10))         #list创建数字列表
for number in numbers:
	if number == 1:
		print(str(number)+"st")   #谨记str()将非字符串值表示为字符串
	elif number == 2:
		print(str(number)+"nd")
	elif number == 3:
		print(str(number)+"rd")
	else:
		print(str(number)+"th")
	
	
