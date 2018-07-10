#coding:gb2312
#读取其他位置的文件
file_path ="C:/Users/HASEE/Desktop/fruits.txt"
with open(file_path) as file_1:
	mes = file_1.read()
	print(mes) 
