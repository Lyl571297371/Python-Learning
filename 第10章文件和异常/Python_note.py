#coding:gb2312
#ϰ��1
filename = 'python_note.txt'

print("��ʽ1����ȡ�����ļ�:\n")
with open(filename) as f:
    contents = f.read()
print(contents)

print("\n\n\n��ʽ2�������ļ�����:\n")
with open(filename) as f:
    for line in f:
        print(line.rstrip())

print("\n\n\n��ʽ3���洢��һ���б��У�����with������ӡ:\n")
with open(filename) as f:
    lines = f.readlines()

for line in lines:
    print(line.rstrip())
