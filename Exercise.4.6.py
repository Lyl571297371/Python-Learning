#coding:gb2312
#练习使用列表的一部分
#切片
names=['ft','zym','hl','cys','ljy','sch']
print("切片练习：")
print(names[-3:-1])#切片用冒号，不包含-1位置的元素
print(names[2:])#不指定的话默认为到最后一个元素终止提取
print(names[:-3])#不指定的话默认为从第一个元素开始提取
print("Here are the first three names on my list"+":")
for friend in names[:3]:#遍历前三个人名
	print(friend.title())
 
#切片复制列表
print("切片复制列表：")
my_friends=names[:]
print("my list names are :")
print(names)
print("\nmy friends are :")
print(my_friends)
names.append('yxf')#添加之后结果就不完全一致了，因为是两个列表各自进行添加的；
my_friends.append('jy')
print("\nmy list names are :")
print(names)
print("\nmy friends are :")
print(my_friends) 

#不切片复制列表
print("不切片复制列表：")
names=my_friends
names.append('yxf')
my_friends.append('jy')
print("\nmy list names are :")
print(names)
print("\nmy friends are :")
print(my_friends)#若使用names=my_friends不切片复制，则是两个列表都指向同一个列表，那进行添加的话两个列表都显示添加的内容
