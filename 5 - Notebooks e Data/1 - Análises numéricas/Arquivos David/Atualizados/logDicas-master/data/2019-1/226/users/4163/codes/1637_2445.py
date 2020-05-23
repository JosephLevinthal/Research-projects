l = input("converter para: ")
x = float(input("valor da temperatura: "))

if(l=="F"):
	c = 5/9*(x-32)
	print(round(c, 2))
else:
	f= (x*9/5)+32
	print(round(f, 2))