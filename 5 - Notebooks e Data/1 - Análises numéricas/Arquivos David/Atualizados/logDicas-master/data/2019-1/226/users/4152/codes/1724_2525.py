num = int(input("Numero: "))
i = 0
a = num / num
var = 1
while (i < num):
	i = i + num % var 
if (num == a):
	print("1 divisor")
else:
	print(i, "divisores")