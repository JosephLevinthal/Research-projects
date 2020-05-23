from numpy import*
from numpy.linalg import*

vet = array(eval(input("digite: ")))

x = array([[5,6,5,15],[10,10,50,20],[10,100,20,40],[100,30,20,35]])

vi = dot(inv(x), vet.T)
		  
print("titica: ", round(vi[0], 0))
print("barro no balde: ", round(vi[1], 0))
print("bestrume: ", round(vi[2], 0))
print("caca de vaca: ", round(vi[3], 0))
		  
if vi[0] == min(vi):
	print("titica")
elif vi[1] == min(vi):
	print("barro no balde")
elif vi[2] == min(vi):
	print("bestrume")
else:
	print("caca de vaca")