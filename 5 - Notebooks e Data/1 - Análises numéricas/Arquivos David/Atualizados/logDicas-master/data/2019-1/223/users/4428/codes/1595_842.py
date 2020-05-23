# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

num = int(input("Digite um numero: "))
soma = 0

while(num > 0):

	resto = num % 10
	num = num//10
	soma = soma+resto

print(soma)