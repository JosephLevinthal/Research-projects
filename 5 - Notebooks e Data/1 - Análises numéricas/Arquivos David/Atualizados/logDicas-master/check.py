from datetime import datetime
from sys import argv,exit
from os import listdir, walk, path
import csv

PATH = "/home/david/dev/dataset/data/2019-1/"
turmas = [222, 223, 224, 225, 226]

for turma in turmas:

  PATH_TURMA = PATH + "/" + str(turma)

  for aluno in listdir(PATH_TURMA + "/users"):

    PATH_ALUNO = PATH + "/" + str(turma) + "/users/" + aluno

    for codemirror in listdir(PATH_ALUNO + "/codemirror"):

      codemirror_file = PATH_ALUNO + "/codemirror/" + codemirror
      file = open(codemirror_file, "r", encoding="UTF-8")
      saida_testar = 0
      id_linha = 0
      saida = ''
      dica_open = 0

      for line in file:      

        if '2019-' in line:
          saida_testar = 0         

        if 'dica_' in line:
          id_linha = id_linha + 1           
          print (id_linha, aluno, line, end="")    

        if saida_testar == 1 and 'Error' in line:
          id_linha = id_linha + 1  
          print (id_linha, aluno, saida, line, end="")             

        if 'saida_testar' in line:
          saida = line.rstrip("\n")
          saida_testar = 1

        if 'dica_open' in line:
          dica_open = id_linha
          # pegar o tempo do open

        if 'dica_close' in line:
          if (id_linha - dica_open == 1):
            print ('sequencia')  
            # pegar o tempo do close
            # calcular o tempo de dica aberta        

