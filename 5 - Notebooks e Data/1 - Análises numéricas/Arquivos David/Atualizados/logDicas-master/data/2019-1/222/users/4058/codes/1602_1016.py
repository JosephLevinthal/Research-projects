# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a=float(input("insira um valor para a:"))
b=float(input("insira um valor para b:"))
c=float(input("insira um valor para c:"))
s=(a+b+c)/2
from math import*
area=sqrt(s*(s-a)*(s-b)*(s-c))
print(round(area, 5))