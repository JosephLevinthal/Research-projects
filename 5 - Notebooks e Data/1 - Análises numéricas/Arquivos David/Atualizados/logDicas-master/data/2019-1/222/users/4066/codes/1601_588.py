# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Use as mensagens de erro para corrigir seu codigo.

valor = int(input("Valor desejado: "))

notas100 = valor // 100
resto100 = valor % 100

notas50 = resto100 // 50
resto50 = resto100 % 50

notas10 = resto50 // 10
resto10 = resto50 % 10

print(notas100)
print(notas50)
print(notas10)