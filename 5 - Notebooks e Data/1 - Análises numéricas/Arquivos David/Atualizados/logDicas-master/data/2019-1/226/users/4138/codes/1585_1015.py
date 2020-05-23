# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
A = int(input("isira o numero:"))
B = int(input("isira o numero:"))
C = int(input("isira o numero:"))

menor = min(A,B,C)
maior = max(A,B,C)
medio = (((A + B +C) - menor)- maior)

print(menor)
print(medio)
print(maior)