#coding:gb2312
#�����ֵ���ϰ��
#ϰ��1
print("ϰ��1��")
fruits={
	'orange':'����',
	'apple ':'ƻ��',      #Ϊ�˴˴����뿴�����ȽϹ����������һ���ո�
	'banana':'�㽶',
	}
fruits['strawberry'] = '��ݮ'    #�ֵ��-ֵ�Ե����
fruits['watermelon'] = '����'
for key ,value in fruits.items():
	print(key +":"+value)
	
	
#ϰ��2
print("\n\nϰ��2��")
messages={
	'nile':'egypt',
	'Yangtze river':'China',
	'Mekong river':'China',
	}
for a,b in messages.items():
	print("The "+a+" runs through "+b+".")
for a in messages.keys():
	print(a.title())
for b in messages.values():
	print(b.title())


#ϰ��3
languages={
	'lyl':'python',
	'ljy':'go',
	'cys':'R',
	}
new_list=['lyl','LJY','hl','cby']
for name in new_list:
	if name.lower() in languages.keys():
		print(name +",лл��������ǵĵ���"+".")
	else:
		print(name+",���ܽ������ǵĵ�����"+"?")

