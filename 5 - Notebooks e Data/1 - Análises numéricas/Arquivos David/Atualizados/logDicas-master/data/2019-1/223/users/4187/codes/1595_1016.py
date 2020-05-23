# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
from math import*
a= float(input("valor do lado a:"))
b= float(input("valor do lado b:"))
c= float(input("valor do lado c:"))

s= (a+b+c)/2
#a = area do triangulo
a= sqrt(s*(s-a)*(s-b)*(s-c))
print(round(a,5))
