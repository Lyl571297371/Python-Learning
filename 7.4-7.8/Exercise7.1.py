#coding:gb2312
#�û������whileѭ��ѧϰ

#input()����
message = "If you tell us who you are ,we can personalize the message you see."
message += "\nWhat is your name?"   #+=���������Ϊ�˴������˶����ַ���
name=input(message)
print("\nHello "+name+"!")

#int()��ȡ��������
age=input("How old are you?")
age=int(age)        #ע�͵����д���ͻ����ԭ����python�޷����ַ������������бȽ�
if age>=18:
	print("You are old enouh to vote"+"!")
else:
	print("Sorry,you will be able to vote when you are a little older"+".")


