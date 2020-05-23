# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
n1 = int(input("numero 1:"))
n2 = int(input("numero 2:"))
n3 = int(input("numero 3:"))
minimo = min(n1,n2,n3)
maximo = max(n1,n2,n3)
intermediario = n1 + n2 + n3 - minimo - maximo
print(minimo)
print(intermediario)
print(maximo)