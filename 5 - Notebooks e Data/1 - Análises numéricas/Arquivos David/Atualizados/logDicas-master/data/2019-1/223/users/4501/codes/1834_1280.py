from numpy import *
from numpy.linalg import*

# Leitura do tabuleiro
tabuleiro = array(eval(input("Tabuleiro: ")))
mov = input("Movimentos: ").upper()
xtab =0 
ytab = 0
moeda = 0
life = 100
for x in mov:
	if(x == 'A'):
		xtab=xtab-1
		if (xtab < 0 or xtab >= shape(tabuleiro)[1]):
			xtab=xtab+1
	elif(x == 'D'):
		xtab=xtab+1
		if(xtab < 0 or xtab >= shape(tabuleiro)[1]):
			xtab=xtab-1
	elif(x == 'W'):
		ytab=ytab-1 
		if(ytab < 0 or ytab >= shape(tabuleiro)[0]):
			ytab=ytab+1
	elif(x == 'S'):
		ytab=ytab+1
		if(ytab < 0 or ytab >= shape(tabuleiro)[0]):
			ytab=ytab-1
	if(tabuleiro[ytab,xtab] == 33):
		if(x == 'A'):
			xtab=xtab+1
		elif(x == 'D'):
			xtab=xtab-1
		elif(x == 'W'):
			ytab=ytab+1 
		elif (x == 'S'):
			ytab=ytab-1
	elif(tabuleiro[ytab,xtab] == 11):
		moeda=moeda+1
		tabuleiro[ytab,xtab] = 0
	elif(tabuleiro[ytab,xtab] == 0):
		moeda=moeda
	elif(tabuleiro[ytab,xtab] == 22):
		life = life - 5

# Imprime saidas
print("posicao x: ", xtab)
print("posicao y: ", ytab)
print("moedas: ", moeda)
print("life: ", life)
