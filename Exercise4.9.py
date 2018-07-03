#coding:gb2312
#元组学习
#元组看起来犹如列表，但是用圆括号而不是方括号来标识，其实就是不可变的列表

dimensions=(200,50)
#print(dimensions[0])   
#print(dimensions[1])   #和访问列表方式一样按索引访问
#dimensions[0]=250      #此处运行会提示错误，因为修改元组的操作是被禁止的，python不能给元组的元素赋值，为继续下面的学习，上面几行代码我注释掉了

#虽然不能修改元组的元素，但可以给存储元组的变量赋值
print("Original Dimensions :")
for dimension in dimensions:    #遍历元组
	print(dimension)
dimensions=(400,100)    #给存储元组的变量重新赋值
print("\nModified Dimensions :")
for dimension in dimensions:    #遍历重新赋值之后的元组
	print(dimension)
  
