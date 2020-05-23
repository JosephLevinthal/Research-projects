from numpy import *
from numpy.linalg import *
m=array(eval(input("matriz: ")))
l=int(input("numero da linha: "))
c=int(input("numero da coluna: "))
if (m[l,c]=="N"):
	print("FOGO")
elif (m[l,c]=="L"):
	print("AGUA")		