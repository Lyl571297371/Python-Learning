#coding:gb2312
#切片练习题和for循环温习

fruits=['banana','watermelon','apple','strawberry','orange']
friend_fruits=fruits[:]#切片复制列表
fruits.append('litchi')
friend_fruits.append('peach')#各自添加
print("My favorite fruits are :")
for items in fruits:
	print(items)
print(fruits)
print("\nMy friend favorite fruits are :")
for items in friend_fruits:
	print(items)
print(friend_fruits)
 
 
