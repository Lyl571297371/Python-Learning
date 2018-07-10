#coding:gb2312
#习题
def make_album(singer_name,album_name):
	infomation = singer_name+' '+album_name
	return infomation
while True:
	print("(Enter 's' at any time to quit)")
	s_name = input("Please enter singer name:  ")
	if s_name == 's':
		break
	a_name =input("Please enter album name:  ")
	if a_name == 's':
		break
	a_inf=make_album(s_name,a_name)
	print(a_inf+"\n\n")
