from numpy import *

mat = array(eval(input("")))

par = 0
impar = 0

for i in range(size(mat)):
	if mat[i] % 2 != 0:
		impar += 1


g2 = zeros(impar, dtype = int)

x = 0 

for k in range(size(mat)):
	
	if mat[k] % 2 != 0:
		g2[x] = mat[k]
		
		x += 1
	
	
print(g2)