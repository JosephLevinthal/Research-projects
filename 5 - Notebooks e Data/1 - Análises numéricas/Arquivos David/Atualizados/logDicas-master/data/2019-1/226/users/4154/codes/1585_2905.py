# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
import math

a = float(input('lado: '))
b = float(input('lado: '))
c = float(input('lado: '))

s = (a+b+c)/2
print(round(math.sqrt(s*(s-a)*(s-b)*(s-c)),5))

