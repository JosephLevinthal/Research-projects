# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
from math import *

var0 = float(input("raio: "))

var1 = var0 ** 2 * pi             # Area
var2 = var0 ** 3 * 4 * pi / 3  # Dominador do Volume

print(round(var1, 3))
print(round(var2, 3))
