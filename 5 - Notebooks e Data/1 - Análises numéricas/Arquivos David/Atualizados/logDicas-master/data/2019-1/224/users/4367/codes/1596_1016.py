# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a= float(input("escolha um numero" ))
b= float(input("escolaha um numero"))
c= float(input("escolha um numero"))
sp= a/2+b/2+c/2
from math import*
area= sqrt((sp*(sp-a)*(sp-b)*(sp-c)))
print(round(area, 5))
