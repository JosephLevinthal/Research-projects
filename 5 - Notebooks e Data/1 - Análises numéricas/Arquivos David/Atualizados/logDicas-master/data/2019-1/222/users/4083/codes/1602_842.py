# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
var = int(input("digite um numero de 4 digitos"))

n1 = var//1000
n2 = (var%1000) // (100)
n3 = ((var%1000) - (n2*100)) // 10
n4 = ((var%1000)-(n2*100+n3*10)) // 1
total = n1 + n2 + n3 + n4
print(total)