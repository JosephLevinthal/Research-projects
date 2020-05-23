# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Use as mensagens de erro para corrigir seu codigo.
valor= int(input("Qual o valor do saque? "))
qtd100=valor // 100
resto_R100 = valor % 100
notas_R50 = resto_R100 // 50
resto_R50 = resto_R100 % 50
notas_R10 = resto_R50 // 10
notas_R100=qtd100
print(int(notas_R100))
print(int(notas_R50))
print(int(notas_R10))