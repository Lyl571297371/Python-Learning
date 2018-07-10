#coding:gb2312
#给文件添加内容
filename = 'write.txt'
with open(filename,'a') as f:
	f.write("\nPython 是一门解释性语言。")
