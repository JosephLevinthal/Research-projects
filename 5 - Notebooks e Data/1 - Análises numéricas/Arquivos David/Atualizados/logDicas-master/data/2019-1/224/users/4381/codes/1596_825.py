# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
raio_r=float(input("raio r"))
from math import *
area_do_circulo= pi*raio_r**2
volume_da_esfera = 4/3*pi*raio_r**3
print(round(area_do_circulo,3))
print(round(volume_da_esfera,3))
