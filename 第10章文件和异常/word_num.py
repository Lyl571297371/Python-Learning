#coding:gb2312
#ʹ�ö���ļ�
def words_num(filename):
	try:
		with open(filename) as f:
			contents = f.read()
	except FileNotFoundError:
		"""
		msg = "Sorry,the file "+filename+" does not exit."
		print(msg)
		"""
		pass         #pass��������pythonʲô����Ҫ��
	else:
		words = contents.split()
		num_words = len(words)
		print(filename.title()+"��ƪ����һ���� "+str(num_words)+" �����ʡ�")
filenames = ['test.txt','pyhton_note.txt','lyl.txt','python_note.txt']
for filename in filenames:
	words_num(filename)
