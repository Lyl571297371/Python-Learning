#coding:gb2312
#ʹ�ñ�־
prompt = "\nTell me something,and i will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
active = True
while active:
	message = input(prompt)
	if message == 'quit':
		break                #�κ�pythonѭ���ж�����ʹ��break����˳�ѭ��������ǰ������б���ֵ��forѭ��
	else:
		print(message)
		
#��ѭ����ʹ��continue
num = 0
while num < 10:
	num += 1
	if num % 2 == 0:
		continue            #continue����python�������µĴ��룬�����ص�ѭ���Ŀ�ͷ
	print(num)
	
