from numpy import *
tabuleiro = array(eval(input("Tabuleiro: ")))
mov = input("Movimentos: ")
xtab = 0
ytab = 0
moeda = 0
life = 100
for x in mov:
   if x == 'A':
        xtab = xtab - 1
   elif x == 'D':
         xtab = xtab + 1
   elif x == 'W':
        ytab = ytab - 1
   elif x == 'S':
        ytab = ytab + 1
   if tabuleiro[ytab,xtab] == 11:
        moeda = moeda + 1
        # Apaga moeda do tabuleiro
        tabuleiro[ytab,xtab] = 0
    # Zumbi
   elif tabuleiro[ytab,xtab] == 22:
        life = life - 5

# Imprime saidas
print("posicao x: ", xtab)
print("posicao y: ", ytab)
print("moedas: ", moeda)
print("life: ", life)
