from datetime import datetime
from sys import argv,exit
from get_time import get_time
from os import listdir, walk, path
from numpy import *
import csv

# Limite de início dos trabalhos válidos
limite_inicio = datetime.strptime("2019-7-31 23:59", "%Y-%m-%d %H:%M")

alunos_colect = {}
alunos_comput = {}
imprimi_cabecalho = 0

with open('dicas_aluno.csv') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')
  for row in csv_reader:
    alunos_colect[int(row[0])] = { 'id_aluno':int(row[0]), 'tipo_dica':'completa' if row[1]=='1' else 'traducao', 'sexo': 'masc' if row[2] == '1' else 'femi', 'nascimento': int(row[3]), 'respondeu_questionario':'nao' if row[4]=='0' else 'sim' }

PATH = "/var/www/cb/codes/dataset/2019-1"
turmas = [222, 223, 224, 225, 226]

for turma in turmas:

  PATH_TURMA = PATH + "/" + str(turma)

  ###################### CRIANDO VETORES DE TRABALHOS (tps e lst) ANTERIORES A 31/07 ##############################

  # guarda os trabalhos do tipo "lista de exercícios"
  trabalhos_lst = [] 

  # guarda os trabalhos do tipo "TP"
  trabalhos_tps = [] 

  # Alimentando os vetores trabalhos_tps e trabalhos_lst
  for trabalho in listdir(PATH_TURMA + "/assessments"):

    trabalho_file = PATH_TURMA + "/assessments/" + trabalho
    file = open(trabalho_file, "r")

    # Verifico se o trabalho ocorreu antes do dia 20/05
    for line in file: 
      if '---- start' in line:
        inicio = line.replace('---- start: ', '')
        inicio = inicio.replace('\n', '')
        inicio = datetime.strptime(inicio, "%Y-%m-%d %H:%M")      

    # Se o trabalho ocorreu antes de 20/05, eu incluo ele em trabalhos_lst ou trabalhos_tps

    trabalho_file = PATH_TURMA + "/assessments/" + trabalho
    file = open(trabalho_file, "r")

    if (inicio < limite_inicio):      
    
      # Classifico o trabalho entre lista e TP
      for line in file: 

        # Ignorando trabalhos Desafio
        if 'Desafio' in line:
          break

        if 'type' in line and 'homework' in line:
          trabalhos_lst.append(trabalho.replace('.data', ''))

        if 'type' in line and 'exam' in line:
          trabalhos_tps.append(trabalho.replace('.data', ''))

  # Ordenando os trabalho na sequencia temporal
  trabalhos_tps.sort() 
  trabalhos_lst.sort() 

  # Caso queira ver os ids dos trabalhos, descomente as linhas abaixo
  #print("Turma ...............: " + str(turma))
  #print("Trabalhos Práticos...: " + str(trabalhos_tps))
  #print("Listas de Exercícios.: " + str(trabalhos_lst))
  #print()

  ###################### CRIANDO JSON DE ALUNOS ##############################

  for aluno in listdir(PATH_TURMA + "/users"):

    PATH_ALUNO = PATH + "/" + str(turma) + "/users/" + aluno
    aluno_json = {}
    n_tp = 0
    n_testes = []
    n_submit = []    
    tempo_na_ide = 0
    tempo_total_na_ide = 0
    quant_exerc_corretos = 0

    if int(aluno) in alunos_colect: 

      # -------------------- Dados Gerais
      aluno_json = alunos_colect[int(aluno)]
      aluno_json['id_aluno'] = int(aluno)              

      # -------------------- Nota dos TPS      
      for trabalho in trabalhos_tps:

        grade_file = PATH_ALUNO + "/grades/" + trabalho + ".log"
        n_tp = n_tp + 1

        # Verificando se o aluno fez o TP
        if path.exists(grade_file):

          file = open(grade_file, "r")

          for line in file: 
            
            if 'grade' in line:

              nota = line.replace('---- grade (0-10): ', '')
              nota = nota.replace('\n', '')
              nota = float(nota)
              if (n_tp<8):
                aluno_json['tp_' + str(n_tp)] = nota               
              else:
                aluno_json['prova_final'] = nota               

        # Caso o aluno não tenha feito o TP, eu atribuo o valor 0 para a nota
        else:

          if (n_tp<8):
            aluno_json['tp_' + str(n_tp)] = "-"
          else:
            aluno_json['prova_final'] = "-"

      # -------------------- Zerando Número de testes
      n_lst = -1
      for trabalho in trabalhos_lst:

        n_lst = n_lst + 1
        aluno_json['n_testes_' + str(n_lst)] = 0

      # -------------------- Zerando Número de testes
      n_lst = -1
      for trabalho in trabalhos_lst:

        n_lst = n_lst + 1
        aluno_json['n_submissoes_' + str(n_lst)] = 0                    

      # -------------------- Zerando Número de exercícios corretos
      n_lst = -1
      for trabalho in trabalhos_lst:

        n_lst = n_lst + 1
        aluno_json['n_exercicios_corretos_' + str(n_lst)] = 0             

      # -------------------- Zerando Tempo Total na IDE
      n_lst = -1
      for trabalho in trabalhos_lst:

        n_lst = n_lst + 1
        aluno_json['total_tempo_ide_' + str(n_lst)] = 0             

      # -------------------- Número de Submissões e testes
      n_lst = -1
      for trabalho in trabalhos_lst:

        executions_folder = PATH_ALUNO + "/executions/" 
        n_lst = n_lst + 1                

        # Para cada arquivo de execução
        for execution_file in listdir(executions_folder):

          # Se o arquivo de execução é de um trabalho em trabalhos_lst
          if execution_file.startswith(trabalho):
            
            file = open(executions_folder + "/" + execution_file, "r")
            for line in file: 
              if '== TEST' in line:
                aluno_json['n_testes_' + str(n_lst)] = aluno_json['n_testes_' + str(n_lst)] + 1
              if '== SUBMITION' in line:
                aluno_json['n_submissoes_' + str(n_lst)] = aluno_json['n_submissoes_' + str(n_lst)] + 1                

      # -------------------- Tempo de resolução dos exercícios
      n_lst = -1
      for trabalho in trabalhos_lst:

        codemirror_folder = PATH_ALUNO + "/codemirror/" 
        executions_folder = PATH_ALUNO + "/executions/" 
        n_lst = n_lst + 1

        # Para cada arquivo de log do codemirror
        for codemirror_file in listdir(codemirror_folder):        

          conseguiu_resolver = 0

          # Se o arquivo de logs do codemirro é de um trabalho em trabalhos_lst
          if codemirror_file.startswith(trabalho): 

            file = open(executions_folder + "/" + codemirror_file, "r")
            for line in file: 
              if '100%' in line:
                conseguiu_resolver = 1  
        
            if (conseguiu_resolver):
              aluno_json['n_exercicios_corretos_' + str(n_lst)] = aluno_json['n_exercicios_corretos_' + str(n_lst)] + 1              
              tempo_na_ide = get_time(codemirror_folder + "/" + codemirror_file)
              aluno_json['total_tempo_ide_' + str(n_lst)] = aluno_json['total_tempo_ide_' + str(n_lst)] + tempo_na_ide

      #print(aluno_json)

      if (imprimi_cabecalho == 0):
        imprimi_cabecalho = 1
        for chave, valor in aluno_json.items(): 
          print(str(chave),end=";")
        print()

      for chave, valor in aluno_json.items(): 
        print(str(valor),end=";")
      print()


