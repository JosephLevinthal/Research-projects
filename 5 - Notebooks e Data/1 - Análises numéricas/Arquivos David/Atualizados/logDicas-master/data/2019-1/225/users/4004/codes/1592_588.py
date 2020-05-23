# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Use as mensagens de erro para corrigir seu codigo.

valor = int(input("Qual o valor? "))

R100V = valor // 100
R100r = valor % 100

R50V = R100r // 50
R50r = R100r % 50

R10V = R50r //10

print(round(R100V, 0))
print(round(R50V, 0))
print(round(R10V, 0))