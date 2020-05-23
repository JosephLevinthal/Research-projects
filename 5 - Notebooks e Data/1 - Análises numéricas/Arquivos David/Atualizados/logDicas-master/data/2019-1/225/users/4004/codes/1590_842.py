# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

abcd = int(input("valor: "))

a = abcd % 10
b = abcd//10 % 10
c = abcd//10//10%10
d = abcd//1000

var1 = a + b + c + d

print(var1)