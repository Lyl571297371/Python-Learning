#coding:gb2312
#����Ͷ�ȡ�û����������
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
