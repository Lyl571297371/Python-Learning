#coding:gb2312
#保存和读取用户输入的数据
import json
filename = 'username.json'
try:
	with open(filename) as f:
		username = json.load(f)
except FileNotFoundError:
	username = input("What's your name?  ")
	with open(filename,'w') as f:
		json.dump(username,f)
		print("We will remember you "+username.title()+"!")
else:
	print("Welcome back,"+username.title()+"!")
