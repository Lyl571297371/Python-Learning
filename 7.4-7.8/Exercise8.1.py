#coding:gb2312
#函数学习 
#定义函数
print("定义函数：")
def hello():            #函数名可以自己怎么喜欢怎么来
	print("Hello Python World!")  
hello()

#向函数传递信息以及实参和形参
print("\n\n\n向函数传递信息以及实参和形参：")
def hello(name):         #此处name就是形参
	print("Hello,"+name.title()+"!")
hello('lyl')    #'lyl'是实参，此处hello('lyl')中，将实参'lyl'传递给了函数hello(),这个值被存储在形参name中
#hello()    #取消掉本行代码注释就会有错误，那是以后为指定了形参，就必须有实参，不然就会出现实参不匹配

