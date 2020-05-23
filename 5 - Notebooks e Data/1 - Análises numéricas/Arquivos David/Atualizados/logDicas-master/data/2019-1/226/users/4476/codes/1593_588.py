# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Use as mensagens de erro para corrigir seu codigo.
a = int(input("valor a ser sacado: "))
notas100 = a//100
notas50 = (a%100)//50
x = notas100*100 + notas50*50
notas10 = (a - x)//10
print(notas100)
print(notas50)
print(notas10)
