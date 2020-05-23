# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
n = int(input("quatro digitos: "))

soma = 0

while (n > 0):
	resto = n % 10
	n = n // 10
	soma += resto
print(n)
print(resto)
print(soma)