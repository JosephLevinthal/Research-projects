# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

import math

a = float(input("Qual o valor do lado a? "))
b = float(input("Qual o valor do lado b? "))
c = float(input("Qual o valor do lado c? "))

s = float((a + b + c)/2)

area = math.sqrt(s*(s-a)*(s-b)*(s-c))

print(round(area, 5))