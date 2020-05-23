from numpy import *
mat = array(eval(input("Digite os numeros de mat dos estudantes: ")))
impar = 0
for n in mat:
	if(n%2 != 0):
		impar = impar + 1
veci = zeros(impar, dtype=int)

i=0
while(i<impar):
	for n in range(size(mat)):
		if(mat[n]%2 != 0):
			veci[i] = mat[n]
			i = i+1
		else:
			i = i
print(veci)	
#i = 0
#n = 0
#while(n < size(veci)):
#	if(mat[i]%2 != 0):
#		veci[n] = mat[i]
#		i = i+1
#		n = n+1
#	i = i+1
#	n = n
#print(veci)	

#j = 0
#for i in v:
#if(i%2 ==0)
	#q[j] = i
	#j+ = 1