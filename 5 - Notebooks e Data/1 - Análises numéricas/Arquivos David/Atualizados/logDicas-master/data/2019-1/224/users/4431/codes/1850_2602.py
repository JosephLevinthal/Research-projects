from numpy import*
from numpy.linalg import*
x=array([[2,1,4],[1,2,0],[2,3,2]])
y=array(eval(input("Digite um vetor: ")))
y=y.T
z=solve(x,y)
print("estafilococo: ",(round(z[0],1)))
print("salmonela: ",(round(z[1],1)))
print("coli: ",(round(z[2],1)))
if(z[0]<z[1] and z[0]<z[2]):
	print("estafilococo")
elif(z[1]<z[0] and z[1]<z[2]):
	print("salmonela")
else:
	print("coli")


		
		
