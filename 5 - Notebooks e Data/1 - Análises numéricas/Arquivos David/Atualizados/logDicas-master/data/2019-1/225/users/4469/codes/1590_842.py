# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
num = int(input("Digita um inteiro de 4 digitos ae, mermao: "))

soma = 0

while num != 0:
	soma += num % 10
	num = num // 10

print(soma)