from numpy import *
from numpy.linalg import *

mg = array(eval(input()))
mg = mg.T

alimentos = array([[2,1,4],[1,2,0],[2,3,2]])

bmp = solve(alimentos,mg)

print("estafilococo:",round(bmp[0],1))
print("salmonela:",round(bmp[1],1))
print("coli:",round(bmp[2],1))

if(bmp[0] == min(bmp)):
	print("estafilococo")
elif(bmp[1] == min(bmp)):
	print("salmonela")
else:
	print("coli")



