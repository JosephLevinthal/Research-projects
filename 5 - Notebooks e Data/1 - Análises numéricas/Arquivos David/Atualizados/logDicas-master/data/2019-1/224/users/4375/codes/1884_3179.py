from numpy import*
mat = array(eval(input("digite a matriz: ")))
d = zeros(size(mat), dtype = int)
cont = 0
for i in range (size(mat)):
	if(mat[i] != 1):
		d[cont] = d[cont]+mat[i]
		cont = cont + 1
for i in range (size(mat)):
	if(mat[i]== 1 ):
		d[cont] = d[cont]+mat[i]
		cont = cont + 1
print(d)
		
	
	