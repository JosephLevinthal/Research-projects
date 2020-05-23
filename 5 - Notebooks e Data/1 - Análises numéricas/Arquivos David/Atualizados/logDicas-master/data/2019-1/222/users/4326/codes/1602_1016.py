# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a=float(input("digite um numero para o lado a do triangolo:"))
b=float(input("digite um numero para o lado b do triangulo:"))
c=float(input("digite um numero para o lado c do triangulo:"))
s =(a+b+c)/2
from math import sqrt
A =sqrt(s*(s-a)*(s-b)*(s-c))
print(round(A,5))