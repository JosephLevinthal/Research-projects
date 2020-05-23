from math import *
vi = (float(input ("valor emprestado:")))
j = float(input("juros do emprestimo:"))
n = (float(input("meses:")))
vf = vi *(1 + j) ** n
print (round(vf,2))