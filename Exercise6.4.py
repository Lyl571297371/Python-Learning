#coding:gb2312
#遍历字典练习题
#习题1
print("习题1：")
fruits={
	'orange':'橘子',
	'apple ':'苹果',      #为了此处代码看起来比较公整我添加了一个空格
	'banana':'香蕉',
	}
fruits['strawberry'] = '草莓'    #字典键-值对的添加
fruits['watermelon'] = '西瓜'
for key ,value in fruits.items():
	print(key +":"+value)
	
	
#习题2
print("\n\n习题2：")
messages={
	'nile':'egypt',
	'Yangtze river':'China',
	'Mekong river':'China',
	}
for a,b in messages.items():
	print("The "+a+" runs through "+b+".")
for a in messages.keys():
	print(a.title())
for b in messages.values():
	print(b.title())


#习题3
languages={
	'lyl':'python',
	'ljy':'go',
	'cys':'R',
	}
new_list=['lyl','LJY','hl','cby']
for name in new_list:
	if name.lower() in languages.keys():
		print(name +",谢谢你接受我们的调查"+".")
	else:
		print(name+",你能接受我们的调查吗"+"?")

