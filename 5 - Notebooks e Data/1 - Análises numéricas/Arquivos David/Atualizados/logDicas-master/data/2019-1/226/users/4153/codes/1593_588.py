# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Use as mensagens de erro para corrigir seu codigo.
valor = int(input("Insira o valor que deseja sacar: "))
R100 = valor // 100
rest100 = valor % 100
R50 = rest100 // 50
rest50 = rest100 % 50
R10 = rest50 // 10
rest10 = rest50 % 10

print(R100)
print(R50)
print(R10)



