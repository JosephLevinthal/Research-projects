# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
import math

r=float(input("valor de r:"))
area=float(round(math.pi*r**2,3))
volume=float(round(4/3*math.pi*r**3,3))
print(area)
print(volume)