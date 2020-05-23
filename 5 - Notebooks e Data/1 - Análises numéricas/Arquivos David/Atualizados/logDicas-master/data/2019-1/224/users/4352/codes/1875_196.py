from numpy import*
from numpy.linalg import*
m = array(eval(input("digite uma matriz NxN (N=N) com as letras B e L: ")))
linha = int(input("digite um numero: "))
coluna = int(input("digite outro numero: "))
l = m.shape[0]
c = m.shape[1]
if m[linha,coluna] == "B".upper():
	print("BOMBA")
elif m[linha,coluna] == "L".upper():
	print("LIVRE")
