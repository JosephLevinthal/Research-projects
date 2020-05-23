# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
from math import*
a=float(input("entre com um lado do triangulo:"))
b=float(input("entre com um segundo lado do triangulo:"))
c=float(input("entre com um terceiro lado do triangulo:"))

s=(a+b+c)/2
x=sqrt((s*(s-a)*(s-b)*(s-c)))

print(round(x, 5))