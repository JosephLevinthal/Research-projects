# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Use as mensagens de erro para corrigir seu codigo.

saque = int(input(" Digite o valor a ser sacado: "))
# Notas de 100.00: 
n1 = saque // 100
b = saque % 100
print (n1)
# Notas de 50.00: 
n2 = (b // 50) 
c = b % 50
print(n2)
# Notas de 10.00: 
n3 = c // 10 
print(n3)