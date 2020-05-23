from numpy import*
from numpy.linalg import*
x = array(eval(input("M:")))
v = array([[2,1,4],[1,2,0],[2,3,2]])
n = dot(inv(v), x.T)
print("estafilococo:", round(n[0],1))
print("salmonela:", round(n[1],1))
print("coli:", round(n[2],1))
if n[0]== min(n):
	print("estafilococo")
elif n[1] == min(n):
	print("salmonela")
else:
	print("coli")