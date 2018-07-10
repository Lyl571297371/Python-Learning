#coding:gb2312
#分析文本
filename = 'test.txt'
try:
	with open(filename) as f:
		infomation = f.read()
except FileNotFoundError:
		msg = ("Sorry,the file "+filename+" does not exit.")
		print(msg)
else:
	"""
	对变量infomation（它现在是一个长长的字符串，包含断箭的全部文本）
	调用方法split(),以生成一个列表,其中包含这个文章中的所有文字
	"""
	words = infomation.split()
	num_words = len(words)
	print("这篇文章一共有 "+str(num_words)+" 个单词。")
