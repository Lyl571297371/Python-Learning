#coding:gb2312
#ϰ��1
print("\n\nϰ��1:")
def city_country(name,country):
	infomation = name+','+country
	return infomation.title()
while True:
	print("please enter city iofomation:  ")
	print("(enter 's' at any time to quit)")
	city_name=input("city_name�� ")
	if city_name == 's':
		break
	other=input("Country:  ")
	if other =='s':
		break
	mes = city_country(city_name,other)
	print(mes+"\n\n")


#ϰ��2
print("\n\nϰ��2:")
def make_album(singer_name,album_name,count=''):
	infomation={'singer':singer_name,'album':album_name}
	if count:
		infomation['count']=count
	return infomation
mes_0 =make_album('xusong','suyan',)
mes_1 =make_album('xianxinghai','guoge','1')
mes_2 =make_album('lyl','chedan')
print(mes_0)	
print(mes_1)
print(mes_2)
