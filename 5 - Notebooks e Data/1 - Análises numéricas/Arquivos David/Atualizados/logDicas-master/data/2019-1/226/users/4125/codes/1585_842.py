# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
numeroloco = int(input("digita um numero de 4 digitos: "))
x1 = numeroloco//1000
x2 = numeroloco//100 - (numeroloco//1000)*10
x3 = numeroloco//10  - (numeroloco//100)*10
x4 = numeroloco//1   - (numeroloco//10)*10
locao = x1 +x2 +x3 +x4
print(locao)