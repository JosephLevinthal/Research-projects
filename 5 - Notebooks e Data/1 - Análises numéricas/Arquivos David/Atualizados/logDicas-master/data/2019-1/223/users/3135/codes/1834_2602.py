from numpy import*
from numpy.linalg import*
ent= array(eval(input("Insira sua entrada:")))

matriarca= array([[2,1,4],[1,2,0],[2,3,2]])

ent=ent.T

quant= dot(inv(matriarca),ent.T)

print("estafilococo:", round(quant[0],1))
print("salmonela:", round(quant[1],1))
print("coli:", round(quant[2],1))

if (quant[0]== min(quant)):
	print("estafilococo")
elif (quant[1]== min(quant)):
	print("salmonela")
else:
	print("coli")