from numpy import *
from numpy.linalg import *
tabuleiro=array(eval(input("vetor: ")))
movi=input("movimento: ").upper()
xtab = 0
ytab = 0
moeda = 0
life = 100
for i in movi :
	if(i == "A"):	
		xtab = xtab - 1
		if(xtab < 0 or xtab >= shape(tabuleiro)[1]):
			xtab = xtab + 1
	elif(i == "D"):
		xtab = xtab + 1
		if(xtab < 0 or xtab >= shape(tabuleiro)[1] ):
			xtab = xtab -1
	elif(i == "W"):
		ytab = ytab - 1
		if(ytab < 0 or ytab >= shape(tabuleiro)[0]):
			ytab = ytab + 1
	elif(i == "S"):
		ytab = ytab + 1
		if(ytab < 0 or ytab >= shape(tabuleiro)[0]):
			ytab = ytab - 1
			
	if(tabuleiro[ytab,xtab] == 33):
		if(i == "A"):
			xtab = xtab + 1
		elif(i == "D"):
			xtab = xtab - 1
		elif(i == "W"):
			ytab = ytab + 1
		elif( i == "S"):
			ytab = ytab - 1
	
	elif(tabuleiro[ytab,xtab] == 11):
		moeda = moeda + 1
		tabuleiro[ytab,xtab] = 0
		
	elif(tabuleiro[ytab,xtab] == 0):
		moeda = moeda
		
	elif(tabuleiro[ytab,xtab] == 22):
		life = life - 5
		
print("posicao x: ", xtab)
print("posicao y: ", ytab)
print("moedas: ", moeda)
print("life: ", life)