#coding:gb2312
#使用多个文件
def words_num(filename):
	try:
		with open(filename) as f:
			contents = f.read()
	except FileNotFoundError:
		"""
		msg = "Sorry,the file "+filename+" does not exit."
		print(msg)
		"""
		pass         #pass语句可以让python什么都不要做
	else:
		words = contents.split()
		num_words = len(words)
		print(filename.title()+"这篇文章一共有 "+str(num_words)+" 个单词。")
filenames = ['test.txt','pyhton_note.txt','lyl.txt','python_note.txt']
for filename in filenames:
	words_num(filename)
