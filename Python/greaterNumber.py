num1 = int(input("enter first number:"))
num2 = int(input("enter first number:"))
num3 = int(input("enter first number:"))
if num1 > num2 and num1 > num3:
	print(num1, "is greater.")
elif num2 > num3:
	print(num2, "is greater.")
else:
	print(num3, "is greater.")