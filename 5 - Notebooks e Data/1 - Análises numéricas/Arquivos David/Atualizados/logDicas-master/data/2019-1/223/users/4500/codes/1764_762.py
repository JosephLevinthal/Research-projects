# Teste
from numpy import *
					  
nome_meses = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])
data = input("Informe a data (ddmmaaaa: ")
dia = int(data[:2])
mes = int(data[3:5])
ano = data[-4:]
# Resultados
nova_data = str(dia) + nome_meses + ano
print(nova_data)
print("17 de janeiro de 1909")