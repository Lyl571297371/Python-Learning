#coding:gb2312

#比较数字
num=18
print(num==18)   #检查两个数字是否相等
print(num<14)    #返回结果为False
print(num<=14)   #返回结果为False
print(num>14)    #返回结果为True
print(num>=18)   #返回结果为True


#检查多个条件
#例如检查两个人是否都小于18岁，and要都满足条件，表达式才为True
age_0= 15
age_1= 19
print((age_0<=18) and (age_1<=18))   #and是测试两个人是否都小于18
age_1=17                      #将age_1改为17
print((age_0<=18) and (age_1<=18))   #返回结果为True


#检查至少有一个人小于18岁,or只需要有一个满足条件，表达式便为True
age_0= 15
age_1= 190
print((age_0<=18) or (age_1<=18))
 
