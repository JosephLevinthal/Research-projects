# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Use as mensagens de erro para corrigir seu codigo.

VALOR = int(input("Qual o valor do saque? "))

# Quantidade de notas de R$ 50
notas_R100 = VALOR//100

# Valor restante a ser sacado com notas menores que R$ 50
resto_R100 = VALOR % 100

# Quantidade de notas de R$ 10
notas_R50 = resto_R100 // 50

# Valor restante a ser sacado com notas menores que R$ 50
resto_R50 = resto_R100 % 50

# Quantidade de notas de R$ 2
notas_R10 = resto_R50 // 10

print(int(notas_R100))
print(int(notas_R50))
print(int(notas_R10))
