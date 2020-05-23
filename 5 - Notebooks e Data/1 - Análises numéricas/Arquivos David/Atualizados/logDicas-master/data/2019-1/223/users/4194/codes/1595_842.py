# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
var = int(input("Digite um numero com quatro digitos: "))
soma = 0
while (var > 0):
	resto = var % 10
	var = var//10
	soma = soma + resto
print(soma)