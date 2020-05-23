from numpy import*
from numpy.linalg import*
#entrada da matriz:
tab=array(eval(input("tabuleiro do jogo: ")))
#entradas da coordenadas
linha= int(input("linha do tabuleiro: "))
coluna= int(input("coluna do tabuleiro: "))
#condiçoes de print
if (tab[linha,coluna]=="B"):
	print("BRANCA")
elif (tab[linha,coluna]=="P"):
	print("PRETA")
elif (tab[linha,coluna]=="V"):
	print("VAZIA")