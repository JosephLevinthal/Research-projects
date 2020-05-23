# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
var1=int(input("qual o valor?"))
var2=int(input("qual o valor?"))
var3=int(input("qual o valor?"))
total1=min(var1,var2,var3)
total2=max(var1,var2,var3)
total3=var1+var2+var3-total1-total2
print(total1)
print(total3)
print(total2)