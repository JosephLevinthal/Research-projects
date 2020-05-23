# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
import math
raio = float(input('digite um numero'))
area = (raio**2)*math.pi
volume = (4*(math.pi*(raio**3)))/3
print(round(area,3))
print(round(volume,3))