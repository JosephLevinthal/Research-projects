# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
from math import*
a=float(input("Lado 1: "))
b=float(input("Lado 2: "))
c=float(input("Lado 3: "))

s=((a+b+c)/(2))
A= (((s)*(s-a)*(s-b)*(s-c))**(1/2))
print(round(A, 5))