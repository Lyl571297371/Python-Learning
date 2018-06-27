#coding:gb2312
#在3.4的基础上，添加一条print语句，指出哪位无法赴约；修改名单，将无法赴约的替换为新的；再次打印一系列信息发出邀请。
Friends=['cby','sch','fjy','lq']
message=", "+"Would You like To Have Dinner With Me"+"?"
print(Friends[-1].title()+", "+"Can't Have Dinner With Me"+".")
Friends[-1]='ljy'
print(Friends[0].title()+message)
print(Friends[1].title()+message)
print(Friends[2].title()+message)
print(Friends[-1].title()+message)
