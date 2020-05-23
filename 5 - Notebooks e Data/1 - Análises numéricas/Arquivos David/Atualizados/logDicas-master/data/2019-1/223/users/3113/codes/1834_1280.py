#######
# Lab 07 – Exercicio 09
# @author: IComp / UFAM
# AVENTURAS COM MOEDAS E ZUMBIS

from numpy import *

# Leitura do tabuleiro
tabuleiro = array(eval(input("Tabuleiro: ")))

# Sequencia de movimentos do personagem
mov = input("Movimentos: ")

# Posicao inicial do personagem
xtab = 0
ytab = 0

# Contadores de atributos do personagem
moeda = 0
life = 100

# Analise da jogada
for x in mov:
   #verificar se posso me mover
	if xtab>0:
		# Move personagem para ESQUERDA
		if x == 'A':
			xtab = xtab-1
			#se tiver coluna
	elif tabuleiro[ytab,xtab] == 33:
		xtab=xtab+1
	#verificar se posso me mover(coluna)
	elif xtab<shape(tabuleiro)[1]:
		# Move personagem para DIREITA
		if x == 'D':
			xtab = xtab+1
			#se tiver coluna
	elif tabuleiro[ytab,xtab] == 33:
		xtab=xtab-1
	#verificar se posso me mover
	elif ytab>=0:
		# Move personagem para CIMA
		if x == 'W':
			ytab = ytab-1
			#se tiver coluna
	elif tabuleiro[ytab,xtab] == 33:
		ytab=ytab+1
	#verificar se posso me mover(linha)
	elif ytab<shape(tabuleiro)[0]:
		# Move personagem para BAIXO
		if x == 'S':        
			ytab = ytab+1
			#se tiver coluna
	elif tabuleiro[ytab,xtab] == 33:
		ytab=ytab-1
    # Trata evento
	if tabuleiro[ytab,xtab] == 11:
		moeda = moeda+1
       # Apaga moeda do tabuleiro
		tabuleiro[ytab,xtab] = 0
	# Zumbi
	elif tabuleiro[ytab,xtab] == 22:
		life = life-5

# Imprime saidas
print("posicao x: ", xtab)
print("posicao y: ", ytab)
print("moedas: ", moeda)
print("life: ", life)
