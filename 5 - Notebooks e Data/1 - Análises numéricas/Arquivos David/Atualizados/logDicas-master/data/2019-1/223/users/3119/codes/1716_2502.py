num = int(input("Digite o numero: "))


r = 12**0.5
cont = 0
soma = 0
exp = 0
while(cont<num):
	den = (2*cont + 1)*(3**(cont ))
	soma = soma - (-1)**(exp + 1)*r/den
	cont = cont + 1
	exp = exp + 1
		
print(round(soma,8))