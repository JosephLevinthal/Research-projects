# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
import math
a=float(input("valor de a:"))
b=float(input("valor de b"))
c=float(input("valor de c"))
s=((a+b+c)/2)
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print(round(area,5))