#coding:gb2312
#字典-嵌套学习
#嵌套：将一系列字典存储在列表中，或将列表作为值存储再字典中。

#1.将字典存储再列表中
alien_0={'color':'green','points':'5',}
alien_1={'color':'red','points':'10'}
alien_2={'color':'yeloow','points':'15'}

aliens=[alien_0,alien_1,alien_2]
for alien in aliens:
	print(alien)
	
#练习
aliens=[]       #创建一个存储外星人的空列表
for alien_number in range(30):  #重复循环30次
	new_alien = {'color':'green','points':'5','speed':'slow'}  #每循环一次都创建一个外星人，这些外星人特征一样
	aliens.append(new_alien)          #将创建的外星人添加到列表末尾
for alien in aliens[:5]:     #使用切片对列表操作，打印前五个外星人
	print(alien)
print("********")
print("一共有"+str(len(aliens))+"个外星人"+".")  #用len()打印列表长度，说明创建了多少个外星人

