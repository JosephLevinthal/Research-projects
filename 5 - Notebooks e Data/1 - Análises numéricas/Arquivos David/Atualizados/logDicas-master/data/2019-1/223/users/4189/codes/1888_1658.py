from numpy import * 
from numpy.linalg import *
y = zeros(5 ,dtype=int)
x = array(eval(input("paises:"))).split(',')
for i in range(size(x)):
	if(x[i]=="CHN"):
	   y[0]=y[0]+1
	if(x[i]=="JPN"):
		y[1]=y[1]+1
	if(x[i]=="KOR"):
		y[2]=Y[2]+1
	if(x[i]=="MGL"):
		y[3]==y[3]+1
	if(x[i]=="THA"):
		y[4]==y[4]+1
print(y)
