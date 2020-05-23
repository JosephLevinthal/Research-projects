# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
numero = str(input())
x = 0
soma = 0
for x in range (0,4):
	soma = int(numero[x]) + soma
print(soma)