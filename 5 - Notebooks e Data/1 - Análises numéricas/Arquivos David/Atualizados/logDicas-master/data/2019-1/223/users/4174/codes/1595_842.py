# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
x= int(input("Numero: "))

soma = 0

while (x != 0):
	resto = x % 10
	x = (x - resto)//10
	soma= soma + resto
print(soma)