from numpy import*

Eusapia = array(eval(input('Jogadas de E: ')))
Barsanulfo = array(eval(input('Jogadas de B: ')))

posi = 0
vitoriaEU = 0
vitoriaBA = 0 
#condiçao para entrar execultar while : VETORES DO MESMO TAMANHO
if(size(Eusapia) == size(Barsanulfo)): 
	while(posi < size(Eusapia) and posi < size(Barsanulfo) ):
		if(Eusapia[posi] == Barsanulfo[posi]): #EMPATE
			vitoriaEU = vitoriaEU
			vitoriaBA = vitoriaBA
		
		elif(Eusapia[posi] == 33 and Barsanulfo[posi] == 22):
			vitoriaEU = vitoriaEU + 1
		
		elif(Eusapia[posi] == 22  and Barsanulfo[posi] == 33):
			vitoriaBA = vitoriaBA + 1
		
		elif(Eusapia[posi] == 11 and Barsanulfo[posi] == 33):
			vitoriaEU = vitoriaEU + 1
		
		elif(Eusapia[posi] == 33 and Barsanulfo[posi] == 11):
			vitoriaBA = vitoriaBA + 1
		
		posi = posi + 1

	print(size(Eusapia) or  size(Barsanulfo))	
	if(vitoriaEU == vitoriaBA):
		print("EMPATE")
	elif(vitoriaEU > vitoriaBA):
		print("EUSAPIA")
	elif(vitoriaEU < vitoriaBA):
		print("BARSANULFO")
	


