#coding:gb2312
#在3.5程序的基础上，用insert添加一个到名单不同位置；append添加一个到末尾；打印消息发出邀请。
names=[]
#print(names)
names.append('lyl')
names.append('cys')
#print(names)
names.insert(0,'hl')
names.insert(1,'fjy')
#print(names)               #三个Print去掉注释符号可以明确观察到列表从空到存储的前后的变化
message=", "+"Would You Like To Have Dinner With Me"+"?"
print(names[0].title()+message)
print(names[1].title()+message)
print(names[2].title()+message)
print(names[-1].title()+message)
