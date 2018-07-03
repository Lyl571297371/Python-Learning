#coding:gb2312
#条件测试练习题

#条件测试练习
#1
fruit="orange"
print("Is fruit=='orange'? I predict True.")
print(fruit=='orange')
print("\nIs fruit=='apple'? I predict False.")
print(fruit=='apple')

#2
num=23
print("\nIs num ==23 ? I prredict True.")
print(num==23)
print("\nIs num=='22'? I predict False.")
print(num=='22')

#3
time='17:12'
print("\nIs time =='17:12'? I predict True.")
print(time=='17:12')
print("\nIs time =='05:12'? I predict False.")
print(time=='05:12')


#更多的条件测试练习
#1
message="I Love My Family"
print("\n第一题：")
print(message=='I Love My Family')    #检查两个字符串相等
print(message=='I Love MY FaMily')    #检查两个字符串不相等，因为python检查是否相等时区分大小写

#2
name='LYL'
print("\n第二题：")
print(name.lower()=='lyl')      #lower()将字符串转化成小写判断是否相等

#3
num_0=99
num_1=69
print("\n第三题：")
print(num_0==num_1)
print(num_0!=num_1)
print(num_0>num_1)
print(num_0<num_1)
print(num_0>=num_1)
print(num_0<=num_1)              #检查数字的大于等于小于

#4
print("\n第四题：")
num_0=2
num_1=5
print((num_0<=4)and(num_1<=4))   #and要两者都满足
print((num_0<=4)or(num_1<=4))    #or只需一个满足即可

#5
print("\n第五题：")
numbers=[0,1,2,3,4,5]
print(0 in numbers)              #检查特定的值是否包含在列表中
number=6
if number not in numbers:        #检查特定的值是否不包含在列表中
	print("This number  is not in numbers:")
	print(number)                  

