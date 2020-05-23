# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Use as mensagens de erro para corrigir seu codigo.
valor = int(input("saque: "))
notas100 = valor//100
notas50 = (valor%100)//50

x = notas100*100 + notas50*50 

notas10 = (valor - x)//10
print(notas100)
print(notas50)
print(notas10)
