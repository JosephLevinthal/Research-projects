# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
var1=float(input("a="))
var2=float(input("b="))
var3=float(input("c="))
s=(var1+var2+var3)/2
from math import*
A=sqrt(s*(s-var1)*(s-var2)*(s-var3))
print(round(A, 5))