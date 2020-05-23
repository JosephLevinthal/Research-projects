from numpy import*
Eusapia = array(eval(input("jogadas de Eusapia:")))
Barsanulfo = array(eval(input("jogadas de Barsanulfo:")))

i = 0
vitoriaEU = 0
vitoriaBA = 0 
#condiçao para entrar execultar while : VETORES DO MESMO TAMANHO
if(size(Eusapia) == size(Barsanulfo)): 
	while(i < size(Eusapia) and i < size(Barsanulfo) ):
		if(Eusapia[i] == Barsanulfo[i]): #EMPATE
			vitoriaEU = vitoriaEU
			vitoriaBA = vitoriaBA
		
		elif(Eusapia[i] == 33 and Barsanulfo[i] == 22):
			vitoriaEU = vitoriaEU + 1
		
		elif(Eusapia[i] == 22  and Barsanulfo[i] == 33):
			vitoriaBA = vitoriaBA + 1
		
		elif(Eusapia[i] == 11 and Barsanulfo[i] == 33):
			vitoriaEU = vitoriaEU + 1
		
		elif(Eusapia[i] == 33 and Barsanulfo[i] == 11):
			vitoriaBA = vitoriaBA + 1
			
		elif(Eusapia[i] == 11 and Barsanulfo[i] == 22):
			vitoriaBA = vitoriaBA + 1
			
		elif(Eusapia[i] == 22 and Barsanulfo[i] == 11):
			vitoriaEU = vitoriaEU + 1
		
		i = i + 1

	print(size(Eusapia) or  size(Barsanulfo))	
	if(vitoriaEU == vitoriaBA):
		print("EMPATE")
	elif(vitoriaEU > vitoriaBA):
		print("EUSAPIA")
	elif(vitoriaEU < vitoriaBA):
		print("BARSANULFO")
	
	#print(vitoriaEU)
	#print(vitoriaBA)