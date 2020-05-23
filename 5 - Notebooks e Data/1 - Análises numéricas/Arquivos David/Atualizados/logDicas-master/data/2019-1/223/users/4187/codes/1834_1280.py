from numpy import *
from numpy.linalg import *

tabuleiro = array(eval(input("Tabuleiro: "))) # Leitura do tabuleiro
mov = input("Movimentos: ") # Sequencia de movimentos do personagem

xtab = 0	# Posicao inicial do personagem
ytab = 0
moeda = 0	# Contadores de atributos do personagem
life = 100

# Limites do tabuleiro
limcol = shape(tabuleiro)[1]	# Limites colunas
limlinh = shape(tabuleiro)[0]	# Limites linhas

# Analise da jogada
for x in mov:
	if(x == 'A'): 
		if(xtab-1 != -1):
			if(tabuleiro[ytab,xtab-1] != 33):
				xtab = xtab -1 # Move personagem para ESQUERDA
	elif(x == 'D'):     
		if(xtab+1 != limcol):
			if(tabuleiro[ytab,xtab+1]!=33):
				xtab =xtab +1 # Move personagem para DIREITA
	elif(x == 'W'): 
		if(ytab-1 != -1):
			if(tabuleiro[ytab-1,xtab]!=33):
				ytab = ytab -1	# Move personagem para CIMA
	elif x == 'S':
		if(ytab+1 != limlinh):
			if(tabuleiro[ytab+1,xtab]!=33):
				ytab = ytab + 1	# Move personagem para BAIXO

	# Trata evento
	if tabuleiro[ytab,xtab] == 11:	# Moeda
		moeda =moeda +1 
		tabuleiro[ytab,xtab] = 0 # Apaga moeda do tabuleiro
	elif tabuleiro[ytab,xtab] == 22: 
		life = life - 5	# Zumbi
		

# Imprime saidas
print("posicao x: ", xtab)
print("posicao y: ", ytab)
print("moedas: ", moeda)
print("life: ", life)