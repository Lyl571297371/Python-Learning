#coding:gb2312
#if��䴦���б���ϰ��
#ϰ��1 
print("ϰ��1��")
users=['lyl','cby','ft','fjy','cxk']   #��������5���û������б�
for user in users:                     #�����û����б�
	if user=='lyl':           #��ʹ�����ǡ�lyl��ʱ�����һ���ʺ���Ϣ
		print("Hello Lyl,would you like to see a status report?")
	else:                     #�������˵�ʱ���������һ����Ϣ
		print("Hello "+user.title()+",thank you for logging in again.\n\n")
		
#ϰ��2
print("ϰ��2��")
users=['lyl','cby','ft','fjy','cxk'] #�б�Ϊ��ִ��if�����
#popped_users=users.pop(0)
#popped_users=users.pop(0)
#popped_users=users.pop(0)
#popped_users=users.pop(0)
#popped_users=users.pop(0)    #ȡ����ע�ͣ����б�Ϊ��ִ��else�����
if users:
	for user in users:
		print("Hello "+user.title()+",thank you for logging in again.\n")
else:
	print("We need to find some users.")

