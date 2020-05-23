# Teste seu codigo aos poucos.
x = int(input())
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
y = int(x%10)#soma
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
z = int(x//10)
l = int(z%10)#soma
m = int(x//100)
n = int(m%10)#soma
o = int(x//1000)#soma

print(y+l+n+o)
