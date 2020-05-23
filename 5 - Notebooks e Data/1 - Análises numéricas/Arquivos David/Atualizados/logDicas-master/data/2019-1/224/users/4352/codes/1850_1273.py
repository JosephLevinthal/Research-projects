from numpy import*
from numpy.linalg import*
m = ([[ 1 , -1 , 0 , 0],
			  [ 0 , 1 , -1 , 0],
			  [ 0 , 0 , 1 , 0 ],
			  [ 1 , 0 , 0 , 1 ]])
i = array([50, -120, 350, 870])
result = dot(inv(m), i.T)
print(result)