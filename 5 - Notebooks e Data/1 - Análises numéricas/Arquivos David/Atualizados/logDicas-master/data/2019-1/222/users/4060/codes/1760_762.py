from numpy import *
# Vetor contendo o nome dos meses do ano
vet_mes = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])
mes_numero=array([1,2,3,4,5,6,7,8,9,10,11,12])
ddmmaaaa=input(" ")
cont=0
cont_1=0
if(ddmmaaaa[2:4]=='01'):
	mm=(vet_mes[0])
elif(ddmmaaaa[2:4]=='02'):
	mm=(vet_mes[1])
elif(ddmmaaaa[2:4]=='03'):
	mm=(vet_mes[2])
elif(ddmmaaaa[2:4]=='04'):
	mm=(vet_mes[3])
elif(ddmmaaaa[2:4]=='05'):
	mm=(vet_mes[4])
elif(ddmmaaaa[2:4]=='06'):
	mm=(vet_mes[5])
elif(ddmmaaaa[2:4]=='07'):
	mm=(vet_mes[6])
elif(ddmmaaaa[2:4]=='08'):
	mm=(vet_mes[7])
elif(ddmmaaaa[2:4]=='09'):
	mm=(vet_mes[8])
elif(ddmmaaaa[2:4]=='10'):
	mm=(vet_mes[9])
elif(ddmmaaaa[2:4]=='11'):
	mm=(vet_mes[10])
elif(ddmmaaaa[2:4]=='12'):
	mm=(vet_mes[11])	
print(ddmmaaaa[0:2], 'de',mm, 'de' ,ddmmaaaa[4:8] )			

