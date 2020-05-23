# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
x = int(input())

x1 = x//1000
rest1 = x%1000
x2 = rest1//100
rest2 = rest1%100
x3 = rest2//10
rest3 = rest2%10
print (x1+x2+x3+rest3)


