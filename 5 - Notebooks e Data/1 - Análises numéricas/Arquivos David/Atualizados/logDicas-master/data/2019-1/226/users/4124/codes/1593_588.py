# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Use as mensagens de erro para corrigir seu codigo.

valor = int(input("Digite o valor desejado: "))
not100 = valor // 100
rest = valor % 100
not50 = rest // 50
rest50 = rest % 50
not10 = rest50 // 10 
print(not100)
print(not50)
print(not10)
