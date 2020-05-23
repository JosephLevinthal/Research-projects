# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
import math
pi = math.pi
raio = float(input("raio:"))
a = float( pi * (raio**2))
v = float((4/3) * pi * (raio**3))
print(round(a, 3))
print(round(v, 3))