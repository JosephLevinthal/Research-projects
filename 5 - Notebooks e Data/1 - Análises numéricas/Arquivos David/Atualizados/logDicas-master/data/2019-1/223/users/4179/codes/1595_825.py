# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
import math
raio=float(input("valor do raio:"))
area=float(round(math.pi*raio**2,3))
volume=float(round(4/3*math.pi*raio**3,3))
print(area)
print(volume)