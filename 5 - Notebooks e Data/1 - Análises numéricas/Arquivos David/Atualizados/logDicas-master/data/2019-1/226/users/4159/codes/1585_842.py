# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
num = int(input("um numero maior que 1000, menor que 10000 "))
mil = num//1000
restm = num%1000
cem = restm//100
restc = restm%100
dez = restc//10
um = restc%10
print(mil+cem+dez+um)