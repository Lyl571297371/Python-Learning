#coding:gb2312
#����ʵ��
print("λ��ʵ�Σ�")
def favorite_numbers(name,number):
	print("�������ߵ������ǣ�"+name.title())
	print(name.title()+"'s favorite number is "+number+"."+"\n")
favorite_numbers('lyl','1')
favorite_numbers('hl','9')    #�����ǿ��Ե��ö�ε�


#�ؼ���ʵ��
print("\n\n\n�ؼ���ʵ��:")
def favorite_numbers(name,number):
	print("�������ߵ������ǣ�"+name.title())
	print(name.title()+"'s favorite number is "+number+"."+"\n")
favorite_numbers(name='lyl',number='1')
favorite_numbers(number='9',name='hl')   #�����������ơ�ֵ�Դ��ݸ���������ô�ؼ��ֵ�ʵ��˳����޹ؽ�Ҫ��


#Ĭ��ֵ
print("\n\n\nĬ��ֵ��") 
def favorite_numbers(name,number = '1'):   #numberָ������1������þ�����ͨ��ʵ����ָ��number
	print("�������ߵ������ǣ�"+name.title())
	print(name.title()+"'s favorite number is "+number+"."+"\n")
favorite_numbers(name='lf')    #û�и�numberָ��ֵ������ʵ��ָ����Ĭ��ֵ
favorite_numbers(name='lyl')   #������ֵ��ֱ�Ӵ��ݸ��������Ͳ����ٿ��Ǻ���������ʵ�ε�˳��
favorite_numbers(name='hl',number='9')  #��ʾ�ĸ�number�ṩ��ֵ�����python�������βε�Ĭ��ֵ
#��ʹ��Ĭ��ֵʱ�����β��б��б������г�û��Ĭ��ֵ���βΣ����г���Ĭ��ֵ���βΣ�python������ȷ�Ľ��λ��ʵ��

