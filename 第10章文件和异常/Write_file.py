#coding:gb2312
#写入文件 
filename = 'write.txt'
with open(filename,'w') as f:
	"""
	'r'--读取模式
	'w'--写入模式 
	'a'--附加模式
'	r+'--读取和写入文件模式
	"""
	f.write("I love python!\n")
	f.write("Python is very useful!")
