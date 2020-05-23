from numpy import *
tabuleiro = array(eval(input("Tabuleiro: ")))
mov = input("Movimentos: ")
# Posicao inicial do personagem
xtab = 0
ytab = 0
# Contadores de atributos do personagem
moeda = 0
life = 100
linhas= shape(tabuleiro)[0]
colunas= shape(tabuleiro)[1]
for x in mov:
	tx=xtab
	ty=ytab
   #Move personagem para ESQUERDA
	if x == 'A':
		xtab = xtab - 1
    # Move personagem para DIREITA
	elif x == 'D':
		xtab = xtab + 1 
    # Move personagem para CIMA
	elif x == 'W':
		ytab= ytab -1   
	elif x == 'S':
		ytab = ytab +1
	if (xtab>colunas-1):
		xtab=xatb-1
	if (ytab>linhas-1):
		ytab=ytab-1
	if (xtab<0):
		xtab=xtab+1
	if (ytab<0):
		ytab=ytab+1
		
		
	if tabuleiro[ytab,xtab] == 11:
		moeda = moeda + 1 
		tabuleiro[ytab,xtab] = 0
	elif tabuleiro[ytab,xtab] == 22:
		life = life - 5 
	elif tabuleiro[ytab,xtab] == 33:
		xtab=tx
		ytab=ty
print("posicao x: ", xtab)
print("posicao y: ", ytab)
print("moedas: ", moeda)
print("life: ", life)