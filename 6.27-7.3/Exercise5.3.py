#coding:gb2312

#�Ƚ�����
num=18
print(num==18)   #������������Ƿ����
print(num<14)    #���ؽ��ΪFalse
print(num<=14)   #���ؽ��ΪFalse
print(num>14)    #���ؽ��ΪTrue
print(num>=18)   #���ؽ��ΪTrue


#���������
#�������������Ƿ�С��18�꣬andҪ���������������ʽ��ΪTrue
age_0= 15
age_1= 19
print((age_0<=18) and (age_1<=18))   #and�ǲ����������Ƿ�С��18
age_1=17                      #��age_1��Ϊ17
print((age_0<=18) and (age_1<=18))   #���ؽ��ΪTrue


#���������һ����С��18��,orֻ��Ҫ��һ���������������ʽ��ΪTrue
age_0= 15
age_1= 190
print((age_0<=18) or (age_1<=18))
 
