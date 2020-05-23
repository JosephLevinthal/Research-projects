# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Use as mensagens de erro para corrigir seu codigo.
valor=int(input("valor que o cliente quer sacar: "))

notas_R50 = valor // 100

# Valor restante a ser sacado com notas menores que R$ 50
resto_R50 = valor % 100

# Quantidade de notas de R$ 10
notas_R10 = resto_R50 // 50

# Valor restante a ser sacado com notas menores que R$ 50
resto_R10 = resto_R50 % 50

# Quantidade de notas de R$ 2
notas_R2 = resto_R10 // 10

print(int(notas_R50))
print(int(notas_R10))
print(int(notas_R2))
