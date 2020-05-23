from math import *
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a = float(input("insira o lado a"))
b = float(input("insira o lado b"))
c = float(input("insira o lado c"))

s = (a+b+c) / 2
a = sqrt(s*(s-a)*(s-b)*(s-c))
print(round(a,5))