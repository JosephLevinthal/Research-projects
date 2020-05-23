# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
var = int(input())

milhar = var//1000
centena = (var%1000)//100
dezena = (var%100)//10
unidade = (var%1000)%10
print(milhar+centena+dezena+unidade)
