from numpy import *
matriculas=array(eval(input("aa")))
qdt_impares=0
for i in matriculas:
	if(i %2 != 0):
		qdt_impares=qdt_impares+1
vetor_impares=zeros(qdt_impares, dtype=int)
j=0
for elemento in matriculas:
	if(i %2 != 0):
		vetor_impares[j]=elemento
		j=j+1
print(vetor_impares)
		
		
		
		
	


	
		
	

