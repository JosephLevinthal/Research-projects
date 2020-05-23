from numpy import*
vet=zeros(6)
a=array(eval(input("dias de falta: ")))

for i in range(size(a)):
	if(a[i]==2):
		vet[0]=vet[0]+1
	elif(a[i]==3):
		vet[1]=vet[1]+1
	elif(a[i]==4):
		vet[2]=vet[2]+1
	elif(a[i]==5):
		vet[3]=vet[3]+1
	elif(a[i]==6):
		vet[4]=vet[4]+1
	elif(a[i]==7):
		vet[5]=vet[5]+1
b=sum(vet)	
for a in range(size(vet)):
	vet[a]=(vet[a]/b)*100
	vet[a]=round(vet[a],1)
print(vet)