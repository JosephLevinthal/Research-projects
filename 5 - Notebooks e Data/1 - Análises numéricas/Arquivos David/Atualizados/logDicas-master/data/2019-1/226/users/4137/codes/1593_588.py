# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Use as mensagens de erro para corrigir seu codigo.
vl = int(input("Quanto deseja sacar:"))
vl50 = vl//100
rt50 = vl%100
vl10 = rt50//50
rt10 = rt50%50
vl2 = rt10//10
print(vl50)
print(vl10)
print(vl2)