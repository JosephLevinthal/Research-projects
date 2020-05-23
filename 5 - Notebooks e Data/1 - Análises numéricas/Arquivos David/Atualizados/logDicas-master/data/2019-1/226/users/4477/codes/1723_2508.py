# Entradas
n = int(input("Determine k: "))
# Variaveis
soma = 3    # Acumulativa
i = 1       # Contadora
sinal = +1  # Alteração do sinal
# Laço
while (i <= n-1):
	soma = soma + sinal *4/((2*i)*(2*i+1)*(2*i+2))
	sinal = - sinal
	i = i + 1
# Saida
print(round(soma, 8))