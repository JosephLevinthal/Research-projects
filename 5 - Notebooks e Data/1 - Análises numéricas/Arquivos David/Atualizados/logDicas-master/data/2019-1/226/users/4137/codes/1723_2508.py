n = int(input("Numero de vezes:"))

x = 2
y = 3
z = 4
cont = 0
soma = 0
s = 0
e = 2
while(cont<n):
	pi = 3 + soma
	soma = soma + 4 / (((x+s)*(y+s)*(z+s))* ((-1)**e))
	e = e + 1
	s = s+2
	cont = cont + 1
print(round(pi, 8))
	
	