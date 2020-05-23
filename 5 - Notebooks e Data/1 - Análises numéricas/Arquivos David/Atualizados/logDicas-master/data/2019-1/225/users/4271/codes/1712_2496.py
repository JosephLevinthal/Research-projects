# Primeiro input
num = int(input("Digite um numero: "))
# zera variavel acumuladora
soma = 0
# Laco de repeticao
while (num != -1):
# Acumula valor
	soma = soma + num
# Inputs seguintes
	num = int(input("Digite outro numero: "))
# Imprimir resultados
print(soma)