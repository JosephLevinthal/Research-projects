from numpy import*
from numpy.linalg import*

v = array(eval(input('Vetor:')))

a = array([[5,6,5,15],
			  [10,10,50,20],
			  [10,100,20,40],
			  [100,30,20,35]])

v = v.T
for i in range(shape(a)[0]):
	u = dot(inv(a), v)

print("titica:",round(u[0], 0))
print("barro no balde:", round(u[1], 0))
print("bestrume:", round(u[2], 0))
print("caca de vaca:", round(u[3], 0))

if(u[0] == min(u)):
	print("titica")
elif(u[1] == min(u)):
	print("barro no balde")
elif(u[2] == min(u)):
	print("bestrume")
elif(u[3] == min(u)):
	print("caca de vaca ")