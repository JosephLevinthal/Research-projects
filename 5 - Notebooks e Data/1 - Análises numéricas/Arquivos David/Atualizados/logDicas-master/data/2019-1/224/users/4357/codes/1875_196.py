from numpy import*
from numpy.linalg import*
matriz=array(eval(input("digite o numero:")))
linha=int(input("digite o numero:"))
coluna=int(input("digite o numero:"))
a=matriz.shape[0]
b=matriz.shape[1]
if(matriz[linha,coluna]=='L'):
	print("LIVRE")
else:
	print("BOMBA")

	