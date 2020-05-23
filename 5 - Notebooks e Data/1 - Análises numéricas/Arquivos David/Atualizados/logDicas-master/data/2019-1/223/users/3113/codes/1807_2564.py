from numpy import*
vet=zeros(3,dtype=int)
a=array(eval(input("gols efetuados por esse time em cada partida:")))
b=array(eval(input("gols efetuados pelo time adversario:")))

for i in range(size(a)):
	if(a[i]>b[i]):
		vet[0]=vet[0]+1
	elif(a[i]==b[i]):
		vet[1]=vet[1]+1
	elif(a[i]<b[i]):
		vet[2]=vet[2]+1
print(vet)