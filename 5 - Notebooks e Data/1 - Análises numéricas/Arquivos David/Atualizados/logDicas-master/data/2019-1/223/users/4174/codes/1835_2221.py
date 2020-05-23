from numpy import*
from numpy.linalg import*

mat = array(eval(input("matriz:")))

Na = shape(mat)[0]

soma = 0 

for i in range(Na):
	soma = soma + min(mat[i, :])
		
media = soma / Na

print(round(media,2))