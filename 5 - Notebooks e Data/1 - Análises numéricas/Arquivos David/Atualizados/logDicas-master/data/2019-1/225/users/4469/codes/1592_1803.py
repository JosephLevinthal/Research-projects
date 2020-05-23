digitos = int(input("Os 4 primeiros digitos da conta bancaria: "))

contador = 2
soma = 0

while(contador < 6):
	soma = soma + ((digitos % 10) * contador)
	digitos = digitos // 10
	contador = contador + 1
	
print(soma % 11)