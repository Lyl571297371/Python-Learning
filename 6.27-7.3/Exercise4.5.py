#coding:gb2312
#�����б���ϰ��2

#����
uneven_number=list(range(1,20,2))
print(uneven_number)
for number in uneven_number:
	print(number)

#3�ı���
number=[value*3 for value in range(1,10)]#3-30���ܱ�3����������������30
print(number)
for value in number:
	print(value)
	
#����
numbers=[]
for value in range(1,10):
	number=value**3
	numbers.append(number)
print(numbers)
for value in numbers:
	print(value)
	
#��������
cubic_number=[value**3 for value in range(1,10)]#������10
print(cubic_number)
for value in cubic_number:
	print(value)
 
