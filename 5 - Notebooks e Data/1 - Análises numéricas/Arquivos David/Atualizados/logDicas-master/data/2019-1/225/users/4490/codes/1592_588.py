# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Use as mensagens de erro para corrigir seu codigo.
v = int(input())

n100 = v//100
r100 = v%100

n50 = r100//50
r50 = r100%50

n10 = r50//10
print(n100)
print(n50)
print(n10)