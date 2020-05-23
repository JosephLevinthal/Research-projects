#######
# Lab 07 – Exercicio 09
# @author: IComp / UFAM
# AVENTURAS COM MOEDAS E ZUMBIS

from numpy import *

# Leitura do tabuleiro
tabuleiro = array(eval(input("Tabuleiro: ")))

# Sequencia de movimentos do personagem
mov = input("Movimentos: ")
l = tabuleiro.shape [0]
c = tabuleiro.shape [1]

# Posicao inicial do personagem
xtab = 0
ytab = 0

# Contadores de atributos do personagem
moeda = 0
life = 100

# Analise da jogada
for x in mov:
	tx = xtab
	ty = ytab
	if x == 'A':
		xtab = xtab - 1
    # Move personagem para DIREITA
	elif x == 'D':
		xtab = xtab + 1
    # Move personagem para CIMA
	elif x == 'W':
		ytab = ytab - 1
	elif x == 'S':
		ytab = ytab + 1
	if tabuleiro[ytab,xtab] == 11:
		moeda = moeda + 1
		tabuleiro[ytab,xtab] = 0
    # Zumbi
	elif tabuleiro[ytab,xtab] == 22:
		life = life - 5
	elif tabuleiro[ytab,xtab] == 33:
		xtab = tx
		ytab = ty

# Imprime saidas
print("posicao x: ", xtab)
print("posicao y: ", ytab)
print("moedas: ", moeda)
print("life: ", life)
