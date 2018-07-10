#coding:gb2312
#存储数据
import json
numbers = [2,3,5,6,7,8,4,9]
filename = 'numbers.json'
with open(filename,'w') as f:
	json.dump(numbers,f)
