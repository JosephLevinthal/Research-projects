# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
var=int(input("digite um numero:"))
var2=int(input("digite um numero: "))
var3=int(input("digite um numero: "))
menor=min(var,var2,var3)
maior=max(var,var2,var3)
meio=var+var2+var3-menor-maior
print(menor)
print(meio)
print(maior)