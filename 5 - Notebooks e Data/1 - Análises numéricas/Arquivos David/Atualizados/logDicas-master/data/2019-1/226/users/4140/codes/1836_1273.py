from numpy import*
from numpy.linalg import*
a=array([[1,-1,0,0],[0,1,-1,0],[0,0,1,0],[1,0,0,1]])
b=array([50,-120,350,870])
b=b.T
re=dot(inv(a),b)
print(re)