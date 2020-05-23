from numpy import*
m=array(eval(input("Matriculas dos estudantes: ")))#Vetor com as matrículas
q=0
for i in range(size(m)):
	
	if(m[i]%2==1):
		q+=1
vetor=zeros(q, dtype=int) # Vetor vazio
j=0
for i in range(size(m)):

	if(m[i]%2==1):
		vetor[j]=vetor[j]+m[i]
		j+=1
print(vetor)