#coding:gb2312
#字典的学习1 
print("字典值的访问和使用：\n")
alien_0 = {'color':'green','points':'5'} #字典用放在花括号{}中的一系列键-值对表示，可以将任何python对象用作字典的值
print("玩家射杀外星人颜色为："+alien_0['color'])       
#new_points=alien_0['points']            #从字典获取与point相关联的值并将其储存到新的变量new_points中
print("玩家获得分数: "+alien_0['points'])     #要访问字典只需要指定字典名和方括号内的键


#添加键-值对
print("\n\n字典添加键-值对：\n")
print(alien_0)
alien_0['x_position']=0
alien_0['y_position']=250
print(alien_0)      #键-值对的排列顺序与添加顺序不同，python不关心键-值对的添加顺序，只关心键和值之间的关联关系


#字典的修改
#例子1
print("\n\n例子1：字典的修改")            #永久性修改
alien_1={}
alien_1['color']='red'
alien_1['points']=10
alien_1['x_position']=50
alien_1['y_position']=300
print("原始字典是：")
print(alien_1)
alien_1['color']='yellow'
print("修改后的外星人颜色现在是： "+alien_1['color']+".")
print("现在的字典是：")
print(alien_1)           

#例子2
print("\n\n例子2：字典的修改")
alien_2={'x_position':0,'y_position':25,'speed':'slow'}
print("Original x_position: "+str(alien_2['x_position']))  #又运行报错，一百遍str()
if alien_2['speed']=='slow':
	x_increment = 1 
elif alien_2['speed']=='medium':
	x_increment = 2
else:
	x_increment = 3
alien_2['x_position']=alien_2['x_position']+x_increment
print("Now x_position is: "+str(alien_2['x_position']))

#字典的键-值对删除
print("\n\n字典的删除：")
print("\n原始字典是:")
print(alien_1)
print("\n删除颜色和分数后的字典:")
del alien_1['color']
del alien_1['points']     #删除的键-值对是永远删除
print(alien_1)

#由类似对象组成的字典
languages={
	'lyl':'python',
	'ljy':'go',
	'cys':'R',
	}
print("\n\nLjy's favorite language is "+languages['ljy'].title()+".")
