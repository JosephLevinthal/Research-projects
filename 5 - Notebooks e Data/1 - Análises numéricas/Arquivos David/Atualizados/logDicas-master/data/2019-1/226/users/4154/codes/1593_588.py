# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Use as mensagens de erro para corrigir seu codigo.
a = int(input('quanto deseja scar? '))

print(a//100)
a = a - (a//100)*100
print(a//50)
a = a - (a//50)*50
print(a//10)