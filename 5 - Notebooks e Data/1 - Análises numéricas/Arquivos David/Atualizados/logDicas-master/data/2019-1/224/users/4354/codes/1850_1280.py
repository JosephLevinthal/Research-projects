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
    # Move personagem para ESQUERDA
	if x == 'A':
		xtab = xtab - 1
    # Move personagem para DIREITA
	elif x == 'D':
		xtab = xtab + 1
    # Move personagem para CIMA
	elif x == 'W':
		ytab = ytab - 1
    # Move personagem para BAIX
	elif x == 'S':
		ytab = ytab + 1
	if (xtab > c - 1):
		xtab = xtab - 1
	if (ytab > l - 1):
		ytab = ytab - 1
	if (xtab < 0):
		xtab = xtab + 1
	if (ytab < 0):
		ytab = ytab + 1
		

	if tabuleiro[ytab,xtab] == 11:
		moeda = moeda + 1 
   		# Apaga moeda do tabuleiro
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
