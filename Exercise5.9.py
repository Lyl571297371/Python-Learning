#coding:gb2312
#if�����ϰ��2

#if-elif-else
age=23
if age<2:
	print("����Ӥ��")
elif 2<=age<4:
	print("��������ѧ��")
elif 4<=age<13:
	print("���Ƕ�ͯ")
elif 13<=age<20:
	print("����������")
elif 20<=age<65:
	print("���ǳ�����")
else:
	print("����������")


#if�����Զ������
fruits=['orange','apple','banana']
if 'apple' in fruits:
	print("Apple is my favorite fruit��")
if 'orange' in fruits:
	print("I really like oranges!")
if 'banana' in fruits:
	print("I really like bananas!")
if 'strawberry' not in fruits:
	print("Please buy some strawberries!")
