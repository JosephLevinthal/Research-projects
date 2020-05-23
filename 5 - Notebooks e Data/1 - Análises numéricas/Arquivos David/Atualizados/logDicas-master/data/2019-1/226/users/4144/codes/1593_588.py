# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Use as mensagens de erro para corrigir seu codigo.
valor = int(input("valor a ser sacado: "))
notas100 = valor // 100
rest100 = valor % 100
notas50 = rest100 // 50
rest50 = rest100 % 50
notas10 = rest50 // 10
print(int(notas100))
print(int(notas50))
print(int(notas10))