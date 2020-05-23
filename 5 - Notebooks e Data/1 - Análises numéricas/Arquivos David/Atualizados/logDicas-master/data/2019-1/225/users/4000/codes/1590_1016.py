# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

x = float(input("Qual o comprimento de x?"))
y = float(input("Qual o comprimento de y?"))
z = float(input("Qual o comprimento de z?"))
s = (x+y+z)/2
from math import*
a = sqrt(s*(s-x)*(s-y)*(s-z))

print(round(a, 5))