# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codi
import math
a = float(input("quanto vale a: "))
b= float(input("quanto vale b: "))
c= float(input("quanto vale c: "))
s = (a+b+c)/2
Z = math.sqrt(s*(s-a)*(s-b)*(s-c))
print(round(Z, 5))