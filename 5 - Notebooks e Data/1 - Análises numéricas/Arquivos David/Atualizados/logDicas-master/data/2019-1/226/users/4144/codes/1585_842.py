# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
x = int(input("digite um numero: "))
y = x // 1000
z = x // 100 - (y * 10)
w = x // 10 - (x // 100) * 10
r = x % w
print (y + z + w + r)
