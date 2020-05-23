# Lab 07 – Exercicio 09
# @author: IComp / UFAM
# AVENTURAS COM MOEDAS E ZUMBIS

from numpy import *

# Leitura do tabuleiro
tabuleiro = array(eval(input("Tabuleiro: ")))
linhas = shape(tabuleiro)[0] -1
colunas = shape(tabuleiro)[1] -1

# Sequencia de movimentos do personagem
mov = input("Movimentos: ")

# Posicao inicial do personagem
x = 0
y = 0

# Contadores de atributos do personagem
moeda = 0
life = 100

# Variáveis para guardar a posição anterior
pos_ant_x = 0
pos_ant_y = 0

# Analise da jogada
for letra in mov:

# Guardar o movimento
	pos_ant_x = x
	pos_ant_y = y

# Atualizar o movimento
	if letra == 'A':	
		x = x - 1

	elif letra == 'D':
		x = x + 1

	elif letra == 'W':	
		y = y - 1
		
	elif letra == 'S':
		y = y + 1
		
# Verificar se o movimento é válido, caso não seja ele permanecerá na posição anterior
	if y < 0:
		y = pos_ant_y
		
	if y > linhas:
		y = pos_ant_y
		
	if x > colunas:
		x = pos_ant_x
	
	if x < 0:
		x = pos_ant_x


# Evento
	# Verificar se foi para o muro
	if tabuleiro[y,x] == 33:
		y = pos_ant_y
		x = pos_ant_x
	# Moeda
	if tabuleiro[y,x] == 11:
		moeda = moeda + 1
	  # Apaga moeda do tabuleiro
		tabuleiro[y,x] = 0
	# Zumbi
	elif tabuleiro[y,x] == 22:
		life = life - 5


print("posicao x: ", x)
print("posicao y: ", y)
print("moedas: ", moeda)
print("life: ", life)	