# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
lados_triangulo_a = float(input("digite o comprimento do lado a: "))
lados_triangulo_b = float(input("digite o comprimento do lado b: "))
lados_triangulo_c = float(input("digite o comprimento do lado c: "))
semiperimetro = (lados_triangulo_a + lados_triangulo_b + lados_triangulo_c) / 2
from math import sqrt
area_triangulo = sqrt(semiperimetro*(semiperimetro-lados_triangulo_a)*(semiperimetro-lados_triangulo_b)*(semiperimetro-lados_triangulo_c))
print(round(area_triangulo,5))