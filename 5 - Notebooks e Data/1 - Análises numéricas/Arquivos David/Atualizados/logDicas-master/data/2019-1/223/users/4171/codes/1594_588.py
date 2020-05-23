valor = int(input("Qual o valor do saque? "))

# Quantidade de notas de R$ 100
notas100 = valor % 100
notas100u = valor // 100
# Valor restante a ser sacado com notas menores que R$ 100
notas100 = notas100 % 100

# Quantidade de notas de R$ 50
notas50 = notas100 // 50

# Valor restante a ser sacado com notas menores que R$ 50
resto50 = notas100 % 50

# Quantidade de notas de R$ 10
notas10 = resto50 // 10

print(int(notas100u))
print(int(notas50))
print(int(notas10))