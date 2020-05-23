# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
var1 = int(input("x"))
var2 = int(input("y"))
var3 = int(input("w"))

r1 = min(var1,var2,var3)
r2 = max(var1,var2,var3)
r3 = var1+var2+var3-r1-r2

print(r1, r3, r2)