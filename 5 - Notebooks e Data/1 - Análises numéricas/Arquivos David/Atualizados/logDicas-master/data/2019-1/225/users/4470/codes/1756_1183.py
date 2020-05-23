from numpy import*
a=array(eval(input("METE AI O VETOR: ")))
i=0 #quantidade de elemento nao negativos
j=0 #copiador
k=0 #controlar a posicao de entrada do vetor
while(k<size(a)): 
	if(a[k]>0):
		i=i+1
	k=k+1
k=0
v=arange(i)
while(k<size(a)):
	if(a[k]>0):
		v[j]=a[k]
		j=j+1
	k=k+1
print(v)

		
	