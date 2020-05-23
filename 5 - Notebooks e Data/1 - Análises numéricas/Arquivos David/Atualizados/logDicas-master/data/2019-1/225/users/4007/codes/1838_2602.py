from numpy import*
from numpy.linalg import*

x = array(eval(input("X,Y,Z: ")))
y = array([[2,1,4],[1,2,0],[2,3,2]])
z = dot(inv(y), x.T)

print("estafilococo: ", round(z[0], 1))
print("salmonela: ", round(z[1], 1))
print("coli: ", round(z[2], 1))

if (z[0] == min(z)):
	print("estafilococo")
elif(z[1] == min(z)):
	print("salmonela")
else:
	print("coli")