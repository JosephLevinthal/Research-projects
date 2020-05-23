from numpy import *
mat = array(eval(input("digite as matriculas: ")))
impar = 0
for i in range(size(mat)):
	if(mat[i]%2!=0):
		impar = impar + 1
k = zeros(impar, dtype=int)
w = 0
for o in range(size(mat)):
	if(mat[o]%2!=0):
		k[w]= mat[o]
		w = w + 1
print(k)