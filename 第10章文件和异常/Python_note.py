#coding:gb2312
#习题1
filename = 'python_note.txt'

print("方式1：读取整个文件:\n")
with open(filename) as f:
    contents = f.read()
print(contents)

print("\n\n\n方式2：遍历文件对象:\n")
with open(filename) as f:
    for line in f:
        print(line.rstrip())

print("\n\n\n方式3：存储在一个列表中，再在with代码块打印:\n")
with open(filename) as f:
    lines = f.readlines()

for line in lines:
    print(line.rstrip())
