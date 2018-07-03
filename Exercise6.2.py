#coding:gb2312
#字典练习题
#习题1
print("习题1：")
infomation={'name':'lyl','age':'23','city':'Yanan'}
print("name: "+infomation['name'])
print("age: "+infomation['age'])
print("city: "+infomation['city'])


#习题2
print("\n\n习题2：")
favorite_numbers={
	'lyl':1,
	'hl':6,
	'cby':9,
	'cys':2,
	'ft':3,
	}
print("Lyl's favorite number is "+str(favorite_numbers['lyl'])+".")
print("Hl's favorite number is "+str(favorite_numbers['hl'])+".")
print("Cby's favorite number is "+str(favorite_numbers['cby'])+".")
print("Cys's favorite number is "+str(favorite_numbers['cys'])+".")
print("Ft's favorite number is "+str(favorite_numbers['ft'])+".")


#习题3
print("\n\n习题3：")
fruits={
	'orange':'橘子',
	'apple ':'苹果',      #为了此处代码看起来比较公整我添加了一个空格
	'banana':'香蕉',
	}
print("orange的翻译：")
print(fruits['orange'])
print("apple 的翻译：")
print(fruits['apple '])   #要注意赋值键-值对的时候添加了不必要的空格也要写进去
print("banana的翻译：")
print(fruits['banana'])
