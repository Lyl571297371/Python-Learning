#coding:gb2312
#����ֵ
def friends(first_name,last_name):   #����ͨ���βν���������
	full_name = last_name + ' '+first_name   #�������ս����һ��洢��full_name��
	return full_name.title()    #��full_name��ֵת��Ϊ����ĸ��д����������ص�����������
friend = friends('yanlong','liu') #������ֵ�洢�ڱ���friend��
print(friend+"\n\n\n")

#�����ֵ�
def build_person(first_name,last_name,age=''):
	person = {'first':first_name.title(),'last':last_name.title()}
	if age:
		person['age']=age
	return person
friends = build_person('yanlong','liu','23')
print(friends)
