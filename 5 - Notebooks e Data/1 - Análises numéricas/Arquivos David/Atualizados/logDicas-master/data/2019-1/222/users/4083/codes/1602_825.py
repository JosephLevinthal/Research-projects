# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
var = float(input("digite o raio"))
from math import*
a = pi*(var**2)
v = (4/3)*pi*(var**3)
print(round(a, 3))
print(round(v, 3))