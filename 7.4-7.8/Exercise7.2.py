#coding:gb2312
#求模运算符（不会指出一个数是另一个数的多少倍，只是指出余数是多少）,适用于判断奇偶数
print(4%3)
print(5%3)
print(6%3)
print(7%3)

#奇偶数的判断
print("\n\n奇偶数的判断：")
number = input("Enter a number, and we will tell you if it's even or odd:")
number = int(number)
if number%2 == 0:
	print(str(number)+" is a even number"+".")
elif number%2 != 0:
	print(str(number)+" is a odd number"+".")


