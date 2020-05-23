from numpy import*
from numpy.linalg import*
tab=array(eval(input()))
a=shape(tab)[0]
b=shape(tab)[1]
life=int(100)
money=int(0)
xtab=int(0)
ytab=int(0)
des=input().upper()
for x in des:
	if x == 'A':
		xtab =xtab-1
		if xtab<0:
			xtab=xtab+1
		if tab[ytab,xtab]== 33:
			xtab=xtab+1
    # Move personagem para DIREITA
	elif x == 'D':
		xtab =xtab +1
		if xtab>b-1:
			xtab=xtab-1
		if tab[ytab,xtab]== 33:
			xtab=xtab-1
    # Move personagem para CIMA
	elif x == 'W':
		ytab =  ytab-1
		if ytab<0:
			ytab=ytab+1
		if tab[ytab,xtab]== 33:
			ytab=ytab+1
		
    # Move personagem para BAIXO
	elif x == 'S':
		ytab = ytab+1
		if ytab>a-1:
			ytab=ytab-1
		if tab[ytab,xtab]== 33:
			ytab=ytab-1
	if tab[ytab,xtab]==11:
		money = money+1
        # Apaga moeda do tabuleiro
		tab[ytab,xtab] = 0
    # Zumbi
	elif tab[ytab,xtab] == 22:
		life = life-5
print("posicao x: ", xtab)
print("posicao y: ", ytab)
print("moedas: ", money)
print("life: ", life)
