#coding:gb2312
#��ϰʹ���б��һ����
#��Ƭ
names=['ft','zym','hl','cys','ljy','sch']
print("��Ƭ��ϰ��")
print(names[-3:-1])#��Ƭ��ð�ţ�������-1λ�õ�Ԫ��
print(names[2:])#��ָ���Ļ�Ĭ��Ϊ�����һ��Ԫ����ֹ��ȡ
print(names[:-3])#��ָ���Ļ�Ĭ��Ϊ�ӵ�һ��Ԫ�ؿ�ʼ��ȡ
print("Here are the first three names on my list"+":")
for friend in names[:3]:#����ǰ��������
	print(friend.title())
 
#��Ƭ�����б�
print("��Ƭ�����б�")
my_friends=names[:]
print("my list names are :")
print(names)
print("\nmy friends are :")
print(my_friends)
names.append('yxf')#���֮�����Ͳ���ȫһ���ˣ���Ϊ�������б���Խ�����ӵģ�
my_friends.append('jy')
print("\nmy list names are :")
print(names)
print("\nmy friends are :")
print(my_friends) 

#����Ƭ�����б�
print("����Ƭ�����б�")
names=my_friends
names.append('yxf')
my_friends.append('jy')
print("\nmy list names are :")
print(names)
print("\nmy friends are :")
print(my_friends)#��ʹ��names=my_friends����Ƭ���ƣ����������б�ָ��ͬһ���б��ǽ�����ӵĻ������б���ʾ��ӵ�����
