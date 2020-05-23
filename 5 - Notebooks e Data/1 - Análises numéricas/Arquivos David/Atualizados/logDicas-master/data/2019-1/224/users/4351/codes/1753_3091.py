#pontuaçoes
#vitoria= 3 
#empate= 1
#derrota=0
pf=0
pm=0
nj=0
resultado= 0
while (resultado!="X"):
	resultado=input("resultado da partida: ").upper()
	if (resultado=="V"):
		pf= pf + 3
		nj=nj+1
	if (resultado=="E"):
		pf= pf + 1
		nj=nj+1
	if (resultado=="D"):
		pf= pf+0
		nj=nj+1
pm= nj*3	
pr= pm-pf
pp= (pr*100)/pm
print(round(pp, 2))
