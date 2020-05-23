from numpy import*
N_matriculas = array(eval(input("Matriculas:")))

impar = 0
for i in range(0,size(N_matriculas)):
	if(N_matriculas[i] % 2 == 1 ):
		impar = impar + 1
		
grupo_2 = zeros(impar, dtype=int)
iN = 0
for i in range(0,size(N_matriculas)):
	if(N_matriculas[i] % 2 == 1):
		if(iN < size(grupo_2)):
			grupo_2[iN] = N_matriculas[i]
			iN = iN + 1
print(grupo_2)
		
			
		
