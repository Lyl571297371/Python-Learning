#coding:gb2312
#ʹ��whileѭ���������б���ֵ�
print("ʹ��whileѭ���������б���ֵ�:")
unconfirmed_users = ['a','b','c','d']
confirmed_users = []
while unconfirmed_users:              #�ڴ���֤�û��б�ѭ��
	current_users = unconfirmed_users.pop()  #�½�һ���б������洢�Ӵ���֤�б�pop������Ԫ��
	print("Verifying Users:  "+current_users)
	confirmed_users.append(current_users)     #�������洢pop��Ԫ���б����ӵ���ʼ�½�������֤�û����б���
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())    #������ab����������ˮ����һ��c���ӵ��Ǹ�����ab�е�ˮ�����е���ô����


#ɾ�������ض�ֵ�������б�Ԫ��
print("\n\nɾ�������ض�ֵ�������б�Ԫ��:")
numbers = ['0','1','1','0','3','5','0','8','0','4']
print(numbers)
while '0' in numbers:   #��number�б��д���0��һֱѭ��
	numbers.remove('0')
print(numbers)


