# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
var1 = int(input(" "))
var2 = int(input(" "))
var3 = int(input(" "))
mim = int(min(var1, var2, var3))
maxx = int(max(var1, var2, var3))
inter = ((var1 + var2 + var3) - mim - maxx)
print(mim)
print(inter)
print(maxx)