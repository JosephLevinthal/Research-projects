# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

x=int(input("valor 1: "))
y=int(input("valor 2: "))
z=int(input("valor 3: "))

m=max(x,y,z)
l=min(x,y,z)
n= x + y + z - l - m
print(l,n,m)