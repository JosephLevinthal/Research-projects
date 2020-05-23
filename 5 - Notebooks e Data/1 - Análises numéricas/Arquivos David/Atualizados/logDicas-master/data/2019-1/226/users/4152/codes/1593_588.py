# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Use as mensagens de erro para corrigir seu codigo.
valor = int(input("Digite aqui o valor total que deseja sacar: "))

q100 = valor // 100

r100 = valor % 100

q50 = r100 // 50

r50 = r100 % 50

q10 = r50 // 10

print(q100)

print(q50)

print(q10)