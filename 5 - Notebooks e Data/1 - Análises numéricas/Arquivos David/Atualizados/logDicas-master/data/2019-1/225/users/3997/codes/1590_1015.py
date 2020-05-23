# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a = int(input())
b = int(input())
c = int(input())

G = max(a,b,c) 
g = min(a,b,c)
j = (a+b+c)-(G+g)
 
print(g)
print(j)
print(G)