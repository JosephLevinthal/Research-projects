# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
num = int(input("Digite o numero: "))

mil = num//1000
cem = num//100 - (mil*10)
dez = num//10 - (mil*100 + cem*10)
uni = num%dez
print(mil + cem + dez + uni)



