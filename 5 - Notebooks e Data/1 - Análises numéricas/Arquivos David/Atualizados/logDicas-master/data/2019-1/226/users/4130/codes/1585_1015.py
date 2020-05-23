# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
nA = int(input("digite o numero A: "))
nB = int(input("digite o numero B: "))
nC = int(input("digite o numero C: "))

vlmin = (min(nA, nB, nC))
vlmax = (max(nA, nB, nC))
vlint = ((nA + nB + nC) - (vlmin + vlmax))

print(vlmin)
print(vlint)
print(vlmax)