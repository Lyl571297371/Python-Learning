#coding:gb2312
#ϰ��2��ʹ��replace()���ַ����е��ض����ʶ��滻Ϊ��һ������
filename = 'python_note.txt'

with open(filename) as f:
    lines = f.readlines()

for line in lines:
    line = line.rstrip()
    print(line.replace('Python', 'C'))  #���ղ��Ǹ������е�ÿһ������'Python'���滻Ϊ'C'
