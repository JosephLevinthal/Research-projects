from numpy import*
from numpy.linalg import*
campo = array(eval(input("campo de batalha:")))

linha = int(input("digite um linha:"))
coluna = int(input("digite uma coluna:"))

if(campo[linha,coluna] == "N"):
	print("FOGO")
elif(campo[linha,coluna] == "L"):
	print("AGUA")