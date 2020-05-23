num1 = int(input( " Digite um numero "))
num2 = int(input(" Digite um numero "))
p = num1 * num2 % 2
if (p==0):
	print(num1 + num2)
else:
	print(num2 - num1)