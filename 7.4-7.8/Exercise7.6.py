#coding:gb2312
#while��ϰ��1
#ϰ��1
print("ϰ��1��")
mes = "What ingredients do you need?"
mes += "\nEnter the ingredients you want to add:  "
active = True
while active:
	message = input(mes)
	if message == 'quit':
		active = False
	else:
		print("\nWe'll add this ingredient to the pizza��"+message+".\n\n\n")
		
		
#ϰ��2
print("\n\nϰ��2��")
message = "How old are you?"
age = ""
active = True
while active:
	age = input(message)
	if age == 'quit':
#		active = False             #ʹ�ñ�־������ѭ��������ʱ��
		break                      #ʹ��break������û�����'quit'ʱ�˳�ѭ��
	elif int(age)<3:
		print("������ѵ�.\n")
	elif 3<=int(age)<12:
		print("����Ʊ����10$.\n")
	elif int(age)>=12:
		print("����Ʊ����15$.\n")
	
	
#ϰ����
print("\n\nϰ��3��û��û�˵�ѭ����ctrl+cֹͣ")
num = 1
while num<=5:
	print(num)  
#	num += 1     #ȡ�����д���ע�ͱ㲻���޽��������ȥ
