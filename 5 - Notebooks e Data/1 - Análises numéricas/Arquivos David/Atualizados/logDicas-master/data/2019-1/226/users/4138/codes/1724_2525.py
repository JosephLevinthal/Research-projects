n = int(input("insira o numero:"))
y = 0
d = 0

while(y < n):
	y = y + 1
	if(n % y == 0):
		print(y)
		d = d + 1
if(d == 1):
	print("1 divisor")
else:
	print(d, "divisores")
		
	
