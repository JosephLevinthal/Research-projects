from numpy import *
# Vetor contendo o nome dos meses do ano
vet_mes = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])
n = input("digite 8 caracteres do dia mes e ano: ")
dd = n[0:2]
mm = n[2:4]
aaaa = n[4:]
mes_ext = vet_mes[int(mm)-1]

print(dd,"de", mes_ext , "de",aaaa)