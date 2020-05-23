# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
nA = int(input("Digite um numero de quatro digitos: "))

nB = nA // 1000
nC = nA // 100 - (nB * 10)
nD = nA // 10 - (nA // 100) * 10
nE = nA % nD

print(nB + nC + nD + nE)