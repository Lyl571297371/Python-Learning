#coding:gb2312
#�����ı�
filename = 'test.txt'
try:
	with open(filename) as f:
		infomation = f.read()
except FileNotFoundError:
		msg = ("Sorry,the file "+filename+" does not exit.")
		print(msg)
else:
	"""
	�Ա���infomation����������һ���������ַ����������ϼ���ȫ���ı���
	���÷���split(),������һ���б�,���а�����������е���������
	"""
	words = infomation.split()
	num_words = len(words)
	print("��ƪ����һ���� "+str(num_words)+" �����ʡ�")
