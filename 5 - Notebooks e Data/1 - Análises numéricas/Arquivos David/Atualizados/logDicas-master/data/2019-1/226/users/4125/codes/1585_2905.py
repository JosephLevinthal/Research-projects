# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
from math import sqrt
a= float(input("digita: "))
b= float(input("digita: "))
c= float(input("digita: "))
s= (a+b+c)/2
a1= sqrt(s*(s-a)*(s-b)*(s-c))
print(round(a1, 5))