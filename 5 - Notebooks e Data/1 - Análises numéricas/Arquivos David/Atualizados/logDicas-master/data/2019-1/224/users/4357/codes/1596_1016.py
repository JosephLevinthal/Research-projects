# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
ladotrianguloa=float(input("digite o comprimento a"))
ladotriangulob=float(input("digite o comprimento b"))
ladotrianguloc=float(input("digite o comprimento c"))
semiperimetro= (ladotrianguloa + ladotriangulob + ladotrianguloc)/2
from math import sqrt
areatriangulo= sqrt(semiperimetro*(semiperimetro-ladotrianguloa)*(semiperimetro-ladotriangulob)*(semiperimetro-ladotrianguloc))
print(round(areatriangulo,5))																						