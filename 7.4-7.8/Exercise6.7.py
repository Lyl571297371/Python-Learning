#coding:gb2312
#Ƕ����ϰ��
#ϰ��1
print("ϰ��1��")
infomation_0={'name':'lyl','age':'23','city':'yanan'}
infomation_1={'name':'cby','age':'20','city':'hunan'}
infomation_2={'name':'ljy','age':'22','city':'shanxi'}
people=[infomation_0,infomation_1,infomation_2]
for value in people:
	print(value)

#ϰ��2
print("\n\nϰ��2��")
pet_0={'����':'hali','����':'��','����':'lq'}
pet_1={'����':'yiyi','����':'è','����':'zxj'}
pet_2={'����':'jiyou','����':'��','����':'������'}
pets=[pet_0,pet_1,pet_2]
for a in pets:
	print(a)

#ϰ��3
print("\n\nϰ��3��")
favorite_places={'lyl':['yunnan','suzhou'],
	'fjy':['guangzhou','xianggang'],
	'ljy':['lasa','xian']}
for a,b in favorite_places.items():   #a���������ֵ�ļ�b�����ֵ��ֵ�����б�
	print(a.title()+"'s favorite places are:")
	for c in b:                 #c�����ֵ�ֵ�����б��ÿһ��Ԫ��
		print("\t"+c.title())

#ϰ��4
print("\n\nϰ��4��")
cities={'yanan':['china','150w','*'],
	'new york':['america','1000w','**'],
	'beijing':['china','1000w','***'],
	}
for names,infomations in cities.items():
	print(names.title()+"����Ϣ(����Ϊ�������ң��˿�������ע��Ϣ)��")
	for infomation in infomations:
		print("\t"+infomation.title())
