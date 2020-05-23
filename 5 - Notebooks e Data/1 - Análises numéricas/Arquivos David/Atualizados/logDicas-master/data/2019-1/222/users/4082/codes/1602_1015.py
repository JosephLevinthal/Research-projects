# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
varA=int(input("numero1:"))
varB=int(input("numero3"))
varC=int(input("numero4"))
total=(varA+varB+varC)
menor =(min(varA,varB,varC))
maior=(max(varA,varB,varC))
totalB=(total-menor-maior)
print(menor)
print(totalB)
print(maior)