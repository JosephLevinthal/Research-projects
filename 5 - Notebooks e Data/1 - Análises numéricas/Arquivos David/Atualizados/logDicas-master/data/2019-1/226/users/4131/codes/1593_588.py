# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Use as mensagens de erro para corrigir seu codigo.
valor = int(input("qual o valor do saque"))
notasR100 = valor // 100
restoR100 = valor % 100
notasR50 = restoR100 // 50
restoR50 = restoR100 % 50
notasR10 = restoR50 // 10
print(int(notasR100))
print(int(notasR50))
print(int(notasR10))
