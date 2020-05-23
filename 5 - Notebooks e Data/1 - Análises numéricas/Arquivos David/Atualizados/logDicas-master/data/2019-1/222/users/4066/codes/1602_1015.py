# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

a = int(input("Insira um valor: "))
b = int(input("Insira um valor: "))
c = int(input("Insira um valor: "))

var1 = min(a,b,c)
var2 = max(a,b,c)
var3 = (a + b + c) - var1 - var2

print(var1)
print(var3)
print(var2)
