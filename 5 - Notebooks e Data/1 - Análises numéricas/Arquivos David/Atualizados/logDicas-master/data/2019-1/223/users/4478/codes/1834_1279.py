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
xtab = 
ytab = 

# Contadores de atributos do personagem
moeda = 
life = 

# Analise da jogada
for x in mov:
    # Move personagem para ESQUERDA
    if x == 'A':
        xtab = 
    # Move personagem para DIREITA
    elif x == 'D':
        xtab = 
    # Move personagem para CIMA
    elif x == 'W':
        ytab = 
    # Move personagem para BAIXO
    elif x == 'S':
        ytab = 

    # Trata evento
    # Moeda
    if tabuleiro[ytab,xtab] == 11:
        moeda = 
        # Apaga moeda do tabuleiro
        tabuleiro[ytab,xtab] = 0
    # Zumbi
    elif tabuleiro[ytab,xtab] == 22:
        life = 

# Imprime saidas
print("posicao x: ", xtab)
print("posicao y: ", ytab)
print("moedas: ", moeda)
print("life: ", life)
