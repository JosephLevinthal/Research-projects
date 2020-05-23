# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Use as mensagens de erro para corrigir seu codigo.
valor = int(input("insira a quantia:"))
n100 = valor//100
resto100 = valor%100

n50 = resto100//50
resto50 = resto100%50

n10 = resto50//10

print(n100)
print(n50)
print(n10)

