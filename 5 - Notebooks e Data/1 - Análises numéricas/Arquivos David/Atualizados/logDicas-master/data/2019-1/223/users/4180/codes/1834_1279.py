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
    # Move personagem para ESQUERDA
	if x == 'A':
		xtab = xtab - 1
    # Move personagem para DIREITA
	elif x == 'D':
 		xtab = xtab + 1
    # Move personagem para CIMA
	elif x == 'W':
		ytab = ytab - 1
    # Move personagem para BAIXO
	elif x == 'S':
		ytab = ytab + 1

    # Trata evento
    # Moeda
	if tabuleiro[ytab,xtab] == 11:
		moeda = moeda + 1
        # Apaga moeda do tabuleiro
		tabuleiro[ytab,xtab] = 0
		moeda = moeda
    # Zumbi
	elif tabuleiro[ytab,xtab] == 22:
		life = life -5

# Imprime saidas
print("posicao x: ", xtab)
print("posicao y: ", ytab)
print("moedas: ", moeda)
print("life: ", life)
