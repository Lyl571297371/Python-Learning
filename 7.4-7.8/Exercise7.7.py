#coding:gb2312
#使用while循环来处理列表和字典
print("使用while循环来处理列表和字典:")
unconfirmed_users = ['a','b','c','d']
confirmed_users = []
while unconfirmed_users:              #在待验证用户列表循环
	current_users = unconfirmed_users.pop()  #新建一个列表用来存储从待验证列表pop出来的元素
	print("Verifying Users:  "+current_users)
	confirmed_users.append(current_users)     #将用来存储pop的元素列表增加到开始新建的以验证用户空列表中
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())    #想起了ab两个杯子有水新增一个c杯子的那个交换ab中的水问题有点那么类似


#删除包含特定值的所有列表元素
print("\n\n删除包含特定值的所有列表元素:")
numbers = ['0','1','1','0','3','5','0','8','0','4']
print(numbers)
while '0' in numbers:   #当number列表中存在0就一直循环
	numbers.remove('0')
print(numbers)


