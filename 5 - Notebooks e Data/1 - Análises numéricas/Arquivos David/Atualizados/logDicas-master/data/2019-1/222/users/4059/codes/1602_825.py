# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
from math import *

r=float(input("Digite o valor do raio:"))
areacirculo=math.pi*r**2
volumecirculo=(4/3)*math.pi*r**3
print(round(areacirculo,3))
print(round(volumecirculo,3))