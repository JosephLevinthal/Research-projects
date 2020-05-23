# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
x = int(input())
y = int(input())
r = int(input())
t = min(x,y,r)
u = max(x,y,r)
v = (y+x+r) - (t +u)
print(t,v,u)