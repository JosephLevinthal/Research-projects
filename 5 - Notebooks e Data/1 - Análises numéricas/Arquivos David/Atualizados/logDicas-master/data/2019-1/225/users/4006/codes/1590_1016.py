# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
from math import*
a=float(input("lado a"))
b=float(input("lado b"))
c=float(input("ladoc"))
s=(a+b+c)/2
d=sqrt(s*(s-a)*(s-b)*(s-c))
print(round(d,5))