#coding:gb2312
#�ֵ��ѧϰ2
#�����ֵ䣬�����ֵ�����м�������ֵ
numbers=[6,9,8]
favorite_numbers={
	'lyl':1,
	'hl':6,
	'cby':9,
	'cys':2,
	'ft':3,
	}
#for name,number in favorite_numbers.items():  #���������������ڱ����ֵ��forѭ��
#	print(name.title()+"'s favorite number is "+str(number)+".\n\n")
print("�б��а�����������")
for name in sorted(favorite_numbers.keys()):  #sorted()����ĸ��������
	print(name.title())
print("�б��а��������֣�")
for number in favorite_numbers.values():
	print(str(number))
	if number not in numbers:
		print(str(number)+"is not in numbers"+".")
		
		
