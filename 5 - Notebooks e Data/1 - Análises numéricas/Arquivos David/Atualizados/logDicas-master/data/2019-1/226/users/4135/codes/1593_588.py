# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Use as mensagens de erro para corrigir seu codigo.
VALOR = int (input("Qual o valor do saque? "))
# Contagem notas de R$100,00
notas_100 = VALOR //100
# Contagem do resto das notas de R$100,00
resto_100 = VALOR%100

# Contagem notas de R$50,00
notas_50 = resto_100//50
# Contagem do resto das notas deR$50,00
resto_50 = VALOR%50

# Contagem notas de R$10,00
notas_10 = resto_50//10

print (notas_100)
print (notas_50)
print (notas_10)