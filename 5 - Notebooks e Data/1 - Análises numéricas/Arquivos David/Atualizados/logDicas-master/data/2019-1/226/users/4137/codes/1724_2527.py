x = int(input("Escreva um numero inteiro:"))

d = 1 
c = 0
d1 = 0

while(d < x):
	y = x % d
	if(y == 0):
		print(d)
		d1 = d1 + d
	d = d+1
if d1==x:
	print("PERFEITO")
else:
	print("NAO PERFEITO")