#coding:gb2312
#if语句练习题1
#if-else
alien_color='yellow'
if alien_color=='green':    #==检查相等；！=检查不等
	print("玩家获得分数5")
else:
	print("玩家获得分数10")


#if-elif-else
alien_color='red'
if alien_color=='green':
	print("玩家你获得分数5")
elif alien_color=='yellow':
	print("玩家获得分数10")
else:
	print("玩家获得分数15")
