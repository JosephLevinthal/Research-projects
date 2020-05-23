# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
import math

a = float(input("digite um numero"))
b = float(input("digite um numero"))
c = float(input("digite um numero"))
sem = (a+b+c)/2
area = math.sqrt(sem*((sem-a)*(sem-b)*(sem-c)))
print(round(area,5))

