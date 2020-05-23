# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
var = int(input("escreva o numero:"))

a = var//1000
b = var//100 - (a * 10)
c = var//10 - ((a * 100) + (b * 10))
d = ((a * 1000) + (b * 100) + (c *10))
e = var -d
print(a + b +c +e)
