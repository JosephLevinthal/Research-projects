# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a =float(input ("Digite o comprimento A:"))
b =float(input ("Digite o comprimento B:"))
c =float(input ("Digite o comprimento C:"))
import math
s = (a + b + c)/2
A = math.sqrt((s*(s-a))*(s-b)*(s-c))
print(round(A,5))