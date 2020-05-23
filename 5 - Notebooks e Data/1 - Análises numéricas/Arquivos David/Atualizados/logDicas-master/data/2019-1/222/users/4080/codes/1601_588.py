# ENTRADA 
VAR = int(input("Qual o valor do saque? "))
# NOTAS DE 100
notas100 = VAR // 100 
# Valor restante a ser sacado com notas menores que R$ 100
resto100 = VAR % 100
# Quantidade de notas de R$ 50
notas50 = resto100 // 50
# Valor restante a ser sacado com notas menores que R$ 100
resto50 = resto100 % 50
# Quantidade de notas de R$ 10
notas10 = resto50 // 10

print(int(notas100))
print(int(notas50))
print(int(notas10))
