from numpy import*
from numpy.linalg import*
a = array(eval(input("CALORIAS: ")))
a = a.T
b =array([[1,2,0.5,1.5],[1.5,1,0.5,1],[1,1,1,2.5],[2.5,0.5,2,0.5]])
c=dot(inv(b),a)
print("caminhada:",round(c[0],0))
print("corrida:",round(c[1],0))
print("bicicleta:",round(c[2],0))
print("natacao:",round(c[3],0))
if(c[0]==max(c)):
	print("caminhada")
elif(c[1]==max(c)):
	print("corrida")
elif(c[2]==max(c)):
	print("bibicleta")
elif(c[3]==max(c)):
	print("natacao")
