num1 = int(input("numero de A: "))
num2 = int(input("numero de B: "))
per1 = float(input("perA: "))
per2 = float(input("perB: "))
num1 = num1 + ((num1 * per1)/100)
num2 = num2 + ((num2 * per2)/100)
n = 1
while(num1 < num2):
	num1 = num1 + ((num1 * per1)/100)
	num2 = num2 + ((num2 * per2)/100)
	n = n + 1
print(n)