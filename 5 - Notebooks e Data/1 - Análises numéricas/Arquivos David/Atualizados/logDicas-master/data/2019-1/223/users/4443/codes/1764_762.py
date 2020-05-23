from numpy import *
data = input("Digite uma data no formato ddmmaaaa: ") #entrada da data no formato solicitado
# Vetor contendo o nome dos meses do ano
vet_mes = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])
im = int(data[2:4]) #indica o numero correspondente ao mes
mes = vet_mes[im-1] #como o vetor comeca na posicao zero, e os meses vao de 1 a 12, e preciso subtrair 1 do valor do mes, para dar a correspondenca correta com a posicao i do vetor dos meses
print(data[:2], "de", mes, "de", data[4:]) #concatena string
