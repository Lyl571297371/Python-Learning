#coding:gb2312
#��ģ�����������ָ��һ��������һ�����Ķ��ٱ���ֻ��ָ�������Ƕ��٣�,�������ж���ż��
print(4%3)
print(5%3)
print(6%3)
print(7%3)

#��ż�����ж�
print("\n\n��ż�����жϣ�")
number = input("Enter a number, and we will tell you if it's even or odd:")
number = int(number)
if number%2 == 0:
	print(str(number)+" is a even number"+".")
elif number%2 != 0:
	print(str(number)+" is a odd number"+".")


