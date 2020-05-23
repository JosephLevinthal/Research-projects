# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
ita = float(input("comprimento a: "))
itb=float(input("comprimento b: "))
itc=float(input("comprimento c:"))
semiperimetro=(ita+itb+itc)/2
from math import *
area_do_triangulo= sqrt(semiperimetro*(semiperimetro-ita)*(semiperimetro-itb)*(semiperimetro-itc))
print (round(area_do_triangulo,5))