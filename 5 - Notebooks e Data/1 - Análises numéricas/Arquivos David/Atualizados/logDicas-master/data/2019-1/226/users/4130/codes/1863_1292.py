from numpy import *
from numpy.linalg import *

m = array(eval(input("Toneladas de minerio: ")))

mine = array([[8,3,1],
				  [5,12,10],
				  [1,3,2]])

k = array(dot(inv(mine),m.T))

w = 0

if(k[0] > k[1] and k[0] > k[2]):
	w = "ametista"
elif(k[1] > k[0] and k[1] > k[2]):
	w = "esmeralda"
else:
	w = "safira"
	
print("ametista: ", round(k[0], 0))
print("esmeralda: ", round(k[1], 0))
print("safira: ", round(k[2], 0))
print(w)