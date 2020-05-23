# Não se esqueça de incluir o módulo numpy
from numpy import *
# Carregar vetor
notas = array([6.2, 2.3, 9.4, 5.1,
8.9, 9.8, 10.0, 7.0, 6.3, 4.4])
# Saida 1: vetor notas
print(notas)
# Saida 2: nota do 3o. aluno
print(notas[2])
# Saida 3: vetor corrigido
notas[4] = notas[4] + 1.0
notas[7] = notas[7] + 1.0
print(notas)