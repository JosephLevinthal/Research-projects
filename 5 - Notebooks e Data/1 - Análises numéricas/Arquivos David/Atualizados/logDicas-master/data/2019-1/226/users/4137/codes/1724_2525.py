x = int(input("Escreva um numero inteiro:"))

d = 1 
c = 0

while(d <= x):
	y = x % d
	if(y == 0):
		print(d)
		c = c + 1
	d = d +1
if(c == 0):
	print("1 divisor")
else:
	print(c, "divisores")