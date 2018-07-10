#coding:gb2312
#嵌套练习题
#习题1
print("习题1：")
infomation_0={'name':'lyl','age':'23','city':'yanan'}
infomation_1={'name':'cby','age':'20','city':'hunan'}
infomation_2={'name':'ljy','age':'22','city':'shanxi'}
people=[infomation_0,infomation_1,infomation_2]
for value in people:
	print(value)

#习题2
print("\n\n习题2：")
pet_0={'名字':'hali','类型':'狗','所属':'lq'}
pet_1={'名字':'yiyi','类型':'猫','所属':'zxj'}
pet_2={'名字':'jiyou','类型':'狗','所属':'刘延龙'}
pets=[pet_0,pet_1,pet_2]
for a in pets:
	print(a)

#习题3
print("\n\n习题3：")
favorite_places={'lyl':['yunnan','suzhou'],
	'fjy':['guangzhou','xianggang'],
	'ljy':['lasa','xian']}
for a,b in favorite_places.items():   #a变量声明字典的键b声明字典的值所属列表
	print(a.title()+"'s favorite places are:")
	for c in b:                 #c声明字典值所属列表的每一个元素
		print("\t"+c.title())

#习题4
print("\n\n习题4：")
cities={'yanan':['china','150w','*'],
	'new york':['america','1000w','**'],
	'beijing':['china','1000w','***'],
	}
for names,infomations in cities.items():
	print(names.title()+"的信息(依次为所属国家，人口数，备注信息)：")
	for infomation in infomations:
		print("\t"+infomation.title())
