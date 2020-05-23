# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Use as mensagens de erro para corrigir seu codigo.

saque = int(input("Digite o valor do saque: "))

nota100 = saque//100

nota50 = (saque%100)//50

nota10 = ((saque%100)%50)//10

print(nota100)
print(nota50)
print(nota10)


