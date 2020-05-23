from numpy import *
tabuleiro= array(eval(input("Tabuleiro: ")))
mov=input("Movimentos: ")
l=tabuleiro.shape [0]
c=tabuleiro.shape [1]

xtab=0
ytab=0
moeda=0
life=100

for x in mov:
	tx=xtab
	ty=ytab
	if x == 'A':
		xtab= xtab - 1
	elif x== 'D':
		xtab= xtab + 1
	elif x=='W':
		ytab= ytab - 1
	elif x == 'S':
		ytab= ytab + 1
	if (xtab > c - 1):
		xtab== xtab - 1
	if (ytab > l - 1):
		ytab= ytab - 1
	if (xtab < 0):
		xtab= xtab + 1
	if (ytab <0):
		ytab= ytab + 1
		
	if tabuleiro[ytab,xtab] == 11:
		moeda= moeda + 1
		tabuleiro[ytab,xtab] = 0
	elif tabuleiro[ytab,xtab] == 22:
		life = life - 5 
	elif tabuleiro[ytab,xtab] == 33:
		xtab= tx
		ytab= ty

print("posicao x: ", xtab)
print("posicao y: ", ytab)
print("moedas: ", moeda)
print("life: ", life)
	
	
	
	
	
	
	
	
	
	
	
	
	
	