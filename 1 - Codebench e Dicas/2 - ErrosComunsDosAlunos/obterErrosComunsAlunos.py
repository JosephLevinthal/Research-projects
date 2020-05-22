import csv
from collections import defaultdict

import pandas as pd

# Cria o vetor que terá os erros que foram tabelados.
pythonErrors = []

# Abre o arquivo com nomes de erro do python.
errorsFile = open('errosPythonTabelados.txt', 'r')

# Popula o vetor de nomes de erro.
for errorName in errorsFile.readlines():
    pythonErrors.append(errorName.strip('\n'))

# Arquivo CSV que será lido
data = pd.read_csv(
    filepath_or_buffer="tabela_submissao_todos_erros_alunos_IPC.csv")

# Cria um defaultdict que recebe inteiros.
errorsCount = defaultdict(int)

i = 1
# coluna do arquivo CSV que será lida
for x in data['executavel_erro']:
    if i % 5000 == 0:
        print(i)

# Encontra os erros na coluna e adiciona ao dicionário
    try:
        for errorName in pythonErrors:
            if errorName in x:
                errorsCount[errorName] += 1
    except:
        None
    i += 1

# Escreve os erros em um arquivo CSV
with open('contagem_erros1.csv', 'w') as f:
    for key in errorsCount.keys():
        f.write("%s,%s\n" % (key, errorsCount[key]))
