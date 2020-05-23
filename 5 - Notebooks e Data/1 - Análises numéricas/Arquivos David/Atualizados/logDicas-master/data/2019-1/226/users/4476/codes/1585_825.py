# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a = float(input("valor do raio: "))
from math import *
area = pi*(a**2)
volume = (4*pi*(a**3))/3 
print(round(area, 3))
print(round(volume, 3))