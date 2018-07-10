#coding:gb2312
#传递实参
print("位置实参：")
def favorite_numbers(name,number):
	print("被调查者的名字是："+name.title())
	print(name.title()+"'s favorite number is "+number+"."+"\n")
favorite_numbers('lyl','1')
favorite_numbers('hl','9')    #函数是可以调用多次的


#关键字实参
print("\n\n\n关键字实参:")
def favorite_numbers(name,number):
	print("被调查者的名字是："+name.title())
	print(name.title()+"'s favorite number is "+number+"."+"\n")
favorite_numbers(name='lyl',number='1')
favorite_numbers(number='9',name='hl')   #将函数的名称—值对传递给参数，那么关键字的实参顺序就无关紧要了


#默认值
print("\n\n\n默认值：") 
def favorite_numbers(name,number = '1'):   #number指定了是1后面调用就无需通过实参来指定number
	print("被调查者的名字是："+name.title())
	print(name.title()+"'s favorite number is "+number+"."+"\n")
favorite_numbers(name='lf')    #没有给number指定值就是用实参指定的默认值
favorite_numbers(name='lyl')   #将名称值对直接传递给函数，就不用再考虑函数调用中实参的顺序
favorite_numbers(name='hl',number='9')  #显示的给number提供了值，因此python将忽略形参的默认值
#在使用默认值时，再形参列表中必须先列出没有默认值的形参，再列出有默认值的形参，python才能正确的解读位置实参


