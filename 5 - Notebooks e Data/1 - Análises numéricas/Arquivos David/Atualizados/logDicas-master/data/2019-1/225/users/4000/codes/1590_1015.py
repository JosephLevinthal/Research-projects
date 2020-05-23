# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
var1 = int(input("Leia o primeiro numero"))
var2 = int(input("Leia o segundo numero"))
var3 = int(input("Leia o terceiro numero"))

a = min(var1, var2, var3)
b = max(var1, var2, var3)
print(a)
print(b)
print(var1 + var2 + var3 - a - b)
