#coding:gb2312
#if���ѧϰ

#�򵥵�if��䣬ִ�����������е�һ��
print("�򵥵�if��䣺\n")
age=18
if age>=18:          #if����for����е����񣬶�Ҫð�ţ���һ�ж�Ҫ����
	print("You are old enough to vote!")   #����if������ͨ���ˣ��Ż����ִ��if���������ĵĴ�����
	print("Have you registersd to vote yet?")


#if-else���
print("\n\nif-else��䣺\n")
age=17
if age>=18:
	print("You are old enough to vote!")
	print("Have you registersd to vote yet?")  #��������age>=18������������ͨ������ִ�д˿�����������
else:
	print("Sorry ,you are too young to vote.")
	print("Please register as soon as you turn 18.")  #age=17������ͨ���������ԣ�����ִ��else������������


#if-elif-else�ṹ�������ڼ�鳬�����������Σ�������һ��ͨ���Ĳ��Խ����������µĲ��ԣ��������������շѵ����ֳ�
print("\n\nif-elif-else�ṹ��\n")
age=23
if age<4:
	print("your admission cost is $0.")   #4���������
elif age<18:                              
	print("your admission cost is $5.")   #4<=age<18�շ�$5
else :
	print("your admission cost is $10.")  #���ڵ���18�շ�$10
#���������������ε�ageֵ���������
#����������⣬�����Դ�������˼���޸�
print("\n\n�޸ĺ�\n")
age=12
if age<4:
	price=0
elif age<18:
	price=5
else:
	price=10
#print("Your admission cost is "+price+".")       ###��һ��д�������������Ϊprice��ֵ��û����str()�����ַ���ֵת��Ϊ�ַ���ֵ
print("Your admission cost is "+"$"+str(price)+".")
#��ϰʹ�ö��elif�����
print("\n\n���elif����飺\n")
age=65
if age<4:
	price=0
elif age<18:
	price=5
elif age>=65:
	price=0
else:
	price=10    
print("Your admission cost is "+"$"+str(price)+".")
#ʡ��else�����
print("\n\nʡ��else����飺\n")
age=65                                     #�ı��˶��ֵ������Ԥ�ڽ��
if age<4:
	price=0
elif 4<=age<18:
	price=5
elif 18<=age<65:
	price=10
elif age>=65:
	price=0
   
print("Your admission cost is "+"$"+str(price)+".")

#�ܽ᣺if-elif-else����һ��ͨ���Ĳ��Ա������Ч�ʸߣ���˵����ֻ��ִ��һ�������
      #�����Ҫ���ж�������Ļ�������һϵ�ж�����if���
     
