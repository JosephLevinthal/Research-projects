# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Use as mensagens de erro para corrigir seu codigo.
valor= int(input("qual valor a ser sacado? "))

cqnt= valor//100
restocqnt=valor%100

dez= restocqnt//50
restodez= restocqnt%50

dois= restodez//10

print(cqnt,dez,dois)