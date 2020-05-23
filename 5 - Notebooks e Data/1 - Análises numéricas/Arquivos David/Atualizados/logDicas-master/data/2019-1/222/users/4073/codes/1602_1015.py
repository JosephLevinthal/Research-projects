# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
varX=int(input("numero 1:"))
varY=int(input("numero 2:"))
varZ=int(input("numero 3:"))
total=(varX+varY+varZ)
menor=(min(varX,varY,varZ))
maior=(max(varX,varY,varZ))
totalX=(total-menor-maior)
print(menor)
print(totalX)
print(maior)