n = int(input("Digite o numero: "))
soma = 0
cont = 0
exp = 0
while(cont<n):
	den = (2*cont + 1)
	soma = soma + (-1)**(exp + 4)*4/ den
	cont = cont + 1
	exp = exp + 1
print(round(soma,8))