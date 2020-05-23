a = int(input("Area total:"))

if (a <= 10000):
	valor = a*5
else:
	mais = a - 10000
	valor = 10000*5 + mais*4
	
print(float(round(valor, 2)))	