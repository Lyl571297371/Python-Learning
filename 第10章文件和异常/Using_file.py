#coding:gb2312
filename = 'pi_digits.txt'
with open(filename) as file_0:
	lines = file_0.readlines()
	pi_string = ''
	for line in lines:
		pi_string += line.strip()
	birthday = input("Please enter your birthday:  ")
	if birthday in pi_string:
		print("Your birthday appears in the pi.")
	else:
		print("Your birthday does not appear in the pi.")
