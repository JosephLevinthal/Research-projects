# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

P = int(input("numero"))

b = P // 1000
x = P % 1000
c = x // 100 
y = x % 100
d = y // 10
z = y % 10
e = z//1
print(b + c + d + e)