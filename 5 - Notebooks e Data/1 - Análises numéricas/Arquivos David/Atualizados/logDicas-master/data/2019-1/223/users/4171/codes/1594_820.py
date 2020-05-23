valor = int(input("Qual o valor do saque?"))

# Quantidade de notas de R$ 50
notas50 = valor % 50
notas50a = valor // 50
# Valor restante a ser sacado com notas menores que R$ 50
notas50 = notas50 % 50

# Quantidade de notas de R$ 10
notas10 = notas50 // 10

# Valor restante a ser sacado com notas menores que R$ 50
resto10 = notas50 % 10

# Quantidade de notas de R$ 2
notas2 = resto10 // 2

print(int(notas50a))
print(int(notas10))
print(int(notas2))