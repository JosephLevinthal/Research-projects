# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a=float(input("Escreva a medida do primeiro lado"))
b=float(input("Escreva a medida do segundo lado"))
c=float(input("Escreva a medida do terceiro lado"))
s=(a+b+c)/2
from math import*
h=sqrt(s*(s-a)*(s-b)*(s-c))
print(round(h,5))
		
