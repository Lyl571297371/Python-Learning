#coding:gb2312
#������ֵ�б�Ͷ��б����һЩ�򵥵Ĳ���
for numbers in range(1,6):#range(1,6)ֻ����1��2��3��4��5��û��6
	print(numbers)

#range���������б�
numbers=list(range(1,6))#list()������ת�����б�
print(numbers)

even_numbers=list(range(2,14,2))#range(x,y,z)x,y��ʾ���ַ�Χ��z��ʾ���������ּ�ľ���
print(even_numbers)

#�Ƚ��������ִ����б�ķ�ʽ
#��һ��
squares=[]
for number in range(1,11): 
	square=number**2
	squares.append(square)
print(squares)

#�ڶ���
squares=[]
for number in range(1,11):
	squares.append(number**2)
print(squares)
 
#������
squares=[number**2 for number in range(1,11)]#nuber**2�Ƕ���ı��ʽ��for number in range(1,11)forѭ�������ڸ����ʽ�ṩֵ
print(squares)

#�������б�ִ�м򵥵�ͳ�Ƽ���
print(min(squares))#�����б���Сֵ
print(max(squares))#�����б����ֵ
print(sum(squares))#�����б�Ԫ�����
