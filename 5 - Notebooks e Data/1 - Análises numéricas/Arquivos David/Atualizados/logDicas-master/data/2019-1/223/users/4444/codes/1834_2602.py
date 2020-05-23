from numpy import *
from numpy.linalg import *
b=array(eval(input("digite:")))
a=array([[2,1,4],[1,2,0],[2,3,2]])
x=dot(inv(a),b)

print("estafilococo: " , round(x[0],1))
print("salmonela: " , round(x[1],1))
print("coli: " , round(x[2],1))

if x[0] == min(x):
    print("estafilococo")
elif x[1] == min(x):
    print("salmonela")
else:
    print("coli")