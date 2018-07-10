#coding:gb2312
#习题2：使用replace()将字符串中的特定单词都替换为另一个单词
filename = 'python_note.txt'

with open(filename) as f:
    lines = f.readlines()

for line in lines:
    line = line.rstrip()
    print(line.replace('Python', 'C'))  #将刚才那个程序中的每一个单词'Python'都替换为'C'
