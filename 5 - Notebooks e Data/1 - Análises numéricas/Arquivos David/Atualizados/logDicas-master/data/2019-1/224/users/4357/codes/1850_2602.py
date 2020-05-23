from numpy import*
from numpy.linalg import*
a=array(eval(input("digite o numero:")))
tabela=([[2,1,4],[1,1,0],[2,3,2]])
r=dot(inv(tabela),a.T)
print("Estafilococo:",round(r[0],1))
print("Salmonela:",round(r[1],1))
print("Coli:",round(r[2],1))
if(r[0]==min(r)):
	print("Estafilococo")
elif(r[1]==min(r)):
	print("Salmonela")
else:
	print("Coli")