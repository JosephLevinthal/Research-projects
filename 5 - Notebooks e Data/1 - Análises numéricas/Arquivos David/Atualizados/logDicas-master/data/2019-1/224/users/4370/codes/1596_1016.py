# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
lta = float(input("comprimento a: "))
ltb = float(input("comprimento b: "))
ltc = float(input("comprimento c: "))
semiperimetro = (lta + ltb + ltc) / 2
from math import sqrt
area_triangulo = sqrt(semiperimetro*(semiperimetro-lta)*(semiperimetro-ltb)*(semiperimetro-ltc))
print(round(area_triangulo,5))