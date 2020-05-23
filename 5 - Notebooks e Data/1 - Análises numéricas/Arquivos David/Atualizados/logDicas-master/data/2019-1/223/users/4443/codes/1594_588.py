# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Use as mensagens de erro para corrigir seu codigo.

valor = int(input("Qual o valor do saque? "))

# Quantidade de notas de R$ 50
n100 = valor // 100

# Valor restante a ser sacado com notas menores que R$ 50
resto1 = valor % 100

# Quantidade de notas de R$50
n50 = resto1 // 50

# Valor restante a ser sacado com notas menores que R$ 50
resto2 = resto1 % 50

# Quantidade de notas de R$ 2
n10 = resto2 // 10

print(int(n100))
print(int(n50))
print(int(n10))

