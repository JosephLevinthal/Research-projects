# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
var1 = float(input("digite o valor de a"))
var2 = float(input("digite o valor de b"))
var3 = float(input("digite o valor de c"))
from math import*
s = (var1 + var2 + var3) / 2
area = sqrt(s*((s - var1)*(s - var2)*(s -var3)))
print(round(area, 5))
