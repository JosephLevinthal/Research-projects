num = int(input(""))

soma = 0
cont = 0
expo = 0
while(cont < num):
	den = (2*cont + 1)
	soma = soma + (-1)**(expo + 4)*4/ den
	cont = cont + 1
	expo = expo + 1
print(round(soma,8))
