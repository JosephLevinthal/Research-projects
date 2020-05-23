# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
import math
a = float(input("valor de a:"))
b = float(input("valor de b:"))
c = float(input("valor de c:"))
S = (a+b+c)/2
area = (S*(S-a)*(S-b)*(S-c))
x = math.sqrt(area)
print(round(x, 5))