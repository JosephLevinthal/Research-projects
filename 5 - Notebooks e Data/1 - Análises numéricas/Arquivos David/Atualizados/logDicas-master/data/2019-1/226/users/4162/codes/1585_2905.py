# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
la=float(input("insira o lado a: "))
lb=float(input("insira o lado b: "))
lc=float(input("insira o lado c: "))
s=(la+lb+lc)/2
a=s*(s-la)*(s-lb)*(s-lc)
from math import*
rz=sqrt(a)
print(round(rz,5))
