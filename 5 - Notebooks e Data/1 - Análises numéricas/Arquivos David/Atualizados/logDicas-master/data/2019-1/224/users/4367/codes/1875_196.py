from numpy import*
from numpy.linalg import*
m=array(eval(input("digite a matriz: ")))
linha=int(input("digite o numero de linhas: "))
coluna=int(input("digite o numero de colunas: "))
l= shape(m)[0]
c= shape(m)[1]

if (m[linha,coluna])=="B".upper():
	print("BOMBA")
if (m[linha,coluna])=="L".upper():
	print ("LIVRE")