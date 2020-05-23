x = int(input("Digite um numero inteiro: "))
d = 0
y = 0
while(y < x):
	y = y + 1
	if(x % y == 0):
		print(y)
		d = d + 1
if(d == 1):
	print(d, "divisor")
else:
	print(d, "divisores")
		
	