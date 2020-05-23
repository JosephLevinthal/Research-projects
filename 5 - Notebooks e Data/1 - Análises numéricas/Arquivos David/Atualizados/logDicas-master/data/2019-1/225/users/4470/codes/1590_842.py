# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
n = int(input())
a = n//1000
ra = n%1000

b = ra//100
rb = ra%100

c = rb//10
rc = rb%10

d = rc//1
rd = rc%1

print(a + b + c + d)


