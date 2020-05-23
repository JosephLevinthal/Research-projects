# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
x = int(input())
a = x//1000
b = x % 1000
c = b // 100
d = b % 100
e = d // 10
f = d % 10
s = a + c + e + f
print(s)