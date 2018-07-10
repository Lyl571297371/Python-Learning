#coding:gb2312
#返回值
def friends(first_name,last_name):   #定义通过形参接受名和姓
	full_name = last_name + ' '+first_name   #将名和姓结合在一起存储在full_name中
	return full_name.title()    #将full_name的值转换为首字母大写并将结果返回到函数调用行
friend = friends('yanlong','liu') #将返回值存储在变量friend中
print(friend+"\n\n\n")

#返回字典
def build_person(first_name,last_name,age=''):
	person = {'first':first_name.title(),'last':last_name.title()}
	if age:
		person['age']=age
	return person
friends = build_person('yanlong','liu','23')
print(friends)
