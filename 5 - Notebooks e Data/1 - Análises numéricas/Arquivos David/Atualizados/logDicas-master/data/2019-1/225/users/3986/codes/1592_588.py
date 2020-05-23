# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Use as mensagens de erro para corrigir seu codigo.
VALOR= int(input("valor a ser sacado: "))

qn100= VALOR // 100
r100 = VALOR % 100

qn50= r100 // 50
r50= r100 % 50

qn10= r50 // 10
r10= r50 % 10

print(int(qn100))
print(int(qn50))
print(int(qn10))

