from numpy import *

# Leitura do tabuleiro
#tabuleiro = array(eval(input("Tabuleiro: ")))
tabuleiro = [[0,0,11,0,0], [0,0,33,22,11], [22,0,11,22,0]]
# Sequencia de movimentos do personagem
#mov = input("Movimentos: ")
mov = "AADDWSDSASSAWSA"
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
	if x == 'D':
		xtab = xtab + 1
    # Move personagem para CIMA
	if x == 'W':
		ytab = ytab - 1
    # Move personagem para BAIXO
	if x == 'S':
		ytab = ytab + 1

    # Trata evento
    # Moeda
	if (tabuleiro [ytab,xtab] == 11):
		moeda = moeda + 1
			   # Apaga moeda do tabuleiro
		tabuleiro[ytab,xtab] = 0
    # Zumbi
	if tabuleiro[ytab,xtab] == 22:
		life = life - 5
	if tabuleiro[ytab,xtab] == 33:
		mov = mov
		

# Imprime saidas
print("posicao x: ", xtab)
print("posicao y: ", ytab)
print("moedas: ", moeda)
print("life: ", life)