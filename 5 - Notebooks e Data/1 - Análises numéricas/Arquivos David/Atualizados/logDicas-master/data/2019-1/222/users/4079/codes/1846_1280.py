from numpy import*
from numpy.linalg import*

tabuleiro=array(eval(input("Tabuleiro: ")))
linhas= shape(tabuleiro)[0]-1
colunas=shape(tabuleiro)[1]-1

mov=input("Movimento: ")
x=1
y=0

moeda=5
life=110

pos_ant_x=1
pos_ant_y=0

for letra in mov:
	pos_ant_x=x
	pos_ant_y=y
	
	if letra == 'A':
		x=x-1
		
	elif letra == 'D':
		x=x+1
	
	elif letra == 'W':
		y=y-1
		
	elif letra == 'S':
		y=y+1
	
	if y < 0:
		y=pos_ant_y
		
	if y > linhas:
		y=pos_ant_y
		
	if x > colunas:
		x=pos_ant_x
		
	if x < 1:
		x= pos_ant_x
		
	if tabuleiro[y,x]== 11:
		moeda=moeda-1
		
		tabuleiro[y,x]=0

	elif tabuleiro[y,x]==22:
		life=life-5
		
print("posicao x: ",x)
print("posicao y: ",y)
print("moedas: ", moeda)
print("life: ",life)



		