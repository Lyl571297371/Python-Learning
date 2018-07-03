#coding:gb2312

#检查特定值是否包含在列表中
fruits=['orange','apple','strawberry']
print('apple' in fruits)     #返回True说明apple在列表中
print("pear" in fruits)      #返回False说明列表中没有pear

#检查特定值是否不包含在列表中
fruits=['orange','apple','strawberry']
fruit="litchi"
if fruit not in fruits:    #如果fruit的值未包含在列表fruits中，python将返回True，进而执行缩进的代码行
	print("please buy some "+fruit+"." )

#术语:布尔表达式,他不过是条件测试的别名，与条件表达式一样，要么为True要么为False
