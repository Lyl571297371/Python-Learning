#coding:gb2312
#使用任意数量的关键字实参  
def build_profile(first,last,**info):
	infomation={}
	infomation['first_name']=first
	infomation['last_name'] =last
	for key,value in info.items():
		infomation[key]=value
	return infomation
inf=build_profile('liu','yanlong',loc='yanan',age='23')
print(inf)
								
