#coding:gb2312
#习题1
print("习题1：")
def make_shirt(size,logo):
	print("该顾客订制的T恤尺码是："+size+".")
	print("该顾客T恤要求的样式是："+logo+"."+"\n\n")
make_shirt('M','pure white')   #位置实参调用函数
make_shirt(logo='pure blank',size='L')  #关键字调用函数


#习题2
print("\n\n习题2:")
def make_shirt(size,logo='i love python'):
	print("该顾客定制的T恤要求是：")
	print("size:"+size+"  logo:"+logo+"\n\n")
make_shirt('M')
make_shirt('L')
make_shirt('XL','ADC')


#习题3
print("\n\n习题3:")
def describe_city(name,country='China'):
	 print(name.title()+" belongs to "+country+".")
describe_city('Yanan')
describe_city('Beijing')
describe_city('Newyork','American')
