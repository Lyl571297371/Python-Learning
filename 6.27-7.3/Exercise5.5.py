#coding:gb2312
#����������ϰ��

#����������ϰ
#1
fruit="orange"
print("Is fruit=='orange'? I predict True.")
print(fruit=='orange')
print("\nIs fruit=='apple'? I predict False.")
print(fruit=='apple')

#2
num=23
print("\nIs num ==23 ? I prredict True.")
print(num==23)
print("\nIs num=='22'? I predict False.")
print(num=='22')

#3
time='17:12'
print("\nIs time =='17:12'? I predict True.")
print(time=='17:12')
print("\nIs time =='05:12'? I predict False.")
print(time=='05:12')


#���������������ϰ
#1
message="I Love My Family"
print("\n��һ�⣺")
print(message=='I Love My Family')    #��������ַ������
print(message=='I Love MY FaMily')    #��������ַ�������ȣ���Ϊpython����Ƿ����ʱ���ִ�Сд

#2
name='LYL'
print("\n�ڶ��⣺")
print(name.lower()=='lyl')      #lower()���ַ���ת����Сд�ж��Ƿ����

#3
num_0=99
num_1=69
print("\n�����⣺")
print(num_0==num_1)
print(num_0!=num_1)
print(num_0>num_1)
print(num_0<num_1)
print(num_0>=num_1)
print(num_0<=num_1)              #������ֵĴ��ڵ���С��

#4
print("\n�����⣺")
num_0=2
num_1=5
print((num_0<=4)and(num_1<=4))   #andҪ���߶�����
print((num_0<=4)or(num_1<=4))    #orֻ��һ�����㼴��

#5
print("\n�����⣺")
numbers=[0,1,2,3,4,5]
print(0 in numbers)              #����ض���ֵ�Ƿ�������б���
number=6
if number not in numbers:        #����ض���ֵ�Ƿ񲻰������б���
	print("This number  is not in numbers:")
	print(number)                  

