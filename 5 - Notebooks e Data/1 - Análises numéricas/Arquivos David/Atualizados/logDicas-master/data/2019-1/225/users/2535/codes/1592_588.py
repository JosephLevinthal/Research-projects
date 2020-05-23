# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Use as mensagens de erro para corrigir seu codigo.

x = int(input())

cem = x//100
x %= 100
cinq = x//50
x %= 50
dez = x//10

print(cem)
print(cinq)
print(dez)