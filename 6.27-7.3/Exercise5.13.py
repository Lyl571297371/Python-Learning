#coding:gb2312
#if��䴦���б���ϰ��
#ϰ��3 
print("ϰ��3:")
current_users = ['lyl','cby','ft','fjy','cxk']
new_users = ['cys','lj','LYL','lf','fjy']
for new_user in new_users:
	if new_user.lower() in current_users:   #ȷ���Ƚ�ʱ�����ִ�Сд
		print("���û����ѱ�ʹ�ã� "+new_user)
	else:
		print("���û�������ʹ�ã� "+new_user)
		
#ϰ��4
print("\n\nϰ��4��")
numbers=list(range(1,10))         #list���������б�
for number in numbers:
	if number == 1:
		print(str(number)+"st")   #����str()�����ַ���ֵ��ʾΪ�ַ���
	elif number == 2:
		print(str(number)+"nd")
	elif number == 3:
		print(str(number)+"rd")
	else:
		print(str(number)+"th")
	
	
