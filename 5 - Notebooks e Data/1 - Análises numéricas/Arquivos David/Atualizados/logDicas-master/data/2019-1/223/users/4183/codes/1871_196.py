from numpy import *
from numpy.linalg import *
m = array(eval(input("Digite a matriz: ")))
l = int(input("Digite a linha: "))
c = int(input("Digite a coluna: "))
if (m[l,c] == "B"):
	print("BOMBA")
elif (m[l,c] == "L"):
	print("LIVRE")