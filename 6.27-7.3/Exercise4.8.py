#coding:gb2312
#��Ƭ��ϰ���forѭ����ϰ

fruits=['banana','watermelon','apple','strawberry','orange']
friend_fruits=fruits[:]#��Ƭ�����б�
fruits.append('litchi')
friend_fruits.append('peach')#�������
print("My favorite fruits are :")
for items in fruits:
	print(items)
print(fruits)
print("\nMy friend favorite fruits are :")
for items in friend_fruits:
	print(items)
print(friend_fruits)
 
 
