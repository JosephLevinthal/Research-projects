# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
from math import*
n=int(input("numero inteiro de quatro digitos:"))

x = n // 1 %10
y = n // 10 % 10
z = n // 100 % 10
w = n // 1000 % 10

xyzw = x + y + z + w

print(xyzw)

