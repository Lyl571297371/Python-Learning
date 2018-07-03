#coding:gb2312
#if语句处理列表练习题
#习题1 
print("习题1：")
users=['lyl','cby','ft','fjy','cxk']   #创建包含5个用户名的列表
for user in users:                     #遍历用户名列表
	if user=='lyl':           #当使用者是‘lyl’时，输出一条问候信息
		print("Hello Lyl,would you like to see a status report?")
	else:                     #是其他人的时候，输出另外一条信息
		print("Hello "+user.title()+",thank you for logging in again.\n\n")
		
#习题2
print("习题2：")
users=['lyl','cby','ft','fjy','cxk'] #列表不为空执行if代码块
#popped_users=users.pop(0)
#popped_users=users.pop(0)
#popped_users=users.pop(0)
#popped_users=users.pop(0)
#popped_users=users.pop(0)    #取消掉注释，则列表为空执行else代码块
if users:
	for user in users:
		print("Hello "+user.title()+",thank you for logging in again.\n")
else:
	print("We need to find some users.")

