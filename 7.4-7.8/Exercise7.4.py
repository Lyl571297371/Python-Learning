#coding:gb2312
#whileѭ�����
print("Whlie ѭ����1����5��")
num = 1
while num <=5:
	print(num)
	num += 1
	
#���û�ѡ���ʱ�˳�
prompt = "\nTell me something,and i will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
message = ''
while message !='quit':
	message=input(prompt)
	if message !='quit':
		print(message)
