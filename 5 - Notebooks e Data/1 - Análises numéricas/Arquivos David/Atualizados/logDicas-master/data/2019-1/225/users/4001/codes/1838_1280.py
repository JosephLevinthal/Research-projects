#######
# Lab 07 – Exercicio 09
# @author: IComp / UFAM
# AVENTURAS COM MOEDAS E ZUMBIS

from numpy import *

# Leitura do tabuleiro
t = array(eval(input("Tabuleiro: ")))

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
	p1 = xtab
	p2 = ytab
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
	if xtab >= shape(t)[1] or ytab >= shape(t)[0] or xtab < 0 or ytab < 0 or t[ytab,xtab] == 33:
		xtab = p1 
		ytab = p2
	if t[ytab,xtab] == 11:
		moeda = moeda + 1
		t[ytab,xtab] = 0
	elif t[ytab,xtab] == 22:
		life = life - 5

# Imprime saidas
print("posicao x: ", xtab)
print("posicao y: ", ytab)
print("moedas: ", moeda)
print("life: ", life)