#coding:gb2312
#使用pop()和del()对列表进行删除操作
names=['cby','lyl','fjy','hl','sch']
message_1="Since the reserved table could not be delivered in time, I could only invite two guests."
print(message_1)
message_2="I'm So Sorry I Can't Have Dinner With You"
popped_names=names.pop(-1)
print(popped_names.title()+", "+message_2+"!")
popped_names=names.pop(-1)
print(popped_names.title()+", "+message_2+"!")
popped_names=names.pop(-1)
print(popped_names.title()+", "+message_2+"!")
#print(names)
message_3=", "+"Would You Like To Have Dinner With Me"+"?"
print(names[0].title()+message_3)
print(names[1].title()+message_3)
del names[0]
del names[0]
print(names)

