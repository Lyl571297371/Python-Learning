#coding:gb2312
#д���ļ� 
filename = 'write.txt'
with open(filename,'w') as f:
	"""
	'r'--��ȡģʽ
	'w'--д��ģʽ 
	'a'--����ģʽ
'	r+'--��ȡ��д���ļ�ģʽ
	"""
	f.write("I love python!\n")
	f.write("Python is very useful!")
