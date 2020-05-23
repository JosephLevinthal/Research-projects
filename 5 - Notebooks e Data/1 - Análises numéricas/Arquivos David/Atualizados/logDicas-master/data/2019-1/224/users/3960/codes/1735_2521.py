n = int(input("Insira um numero: "))
pi = 1.0
d = 1.0
cont = 1

while(cont <= n):
	d = d * (cont / (cont*2+1))
	pi = pi + d
	cont = cont + 1
	
print(round(2*pi,10))