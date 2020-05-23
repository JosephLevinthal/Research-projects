# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
varA = int(input("Numero 1:"))
varB = int(input("Numero 2:"))
varC = int(input("Numero 3:"))
total= (varA+varB+varC)
menor = (min(varA,varB,varC))
maior = (max(varA,varB,varC))
totalA=(total-menor-maior)
print(menor)
print(totalA)
print(maior)

