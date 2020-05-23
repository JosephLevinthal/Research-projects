from numpy import*
m=array(eval(input("entre com vetro:")))
f=array(eval(input("entre com vetro:")))
h=int(input("entre com vetro:"))

vet=zeros(3, dtype=int)

for i in range(0,size(m)):
	if (m[i]>=5 and f[i]>=(0.75*h)):
		vet[0]=vet[0]+1
	elif(m[i]<5):
		vet[1]=vet[1]+1
	elif(f[i]<(0.75*h)):
		vet[2]=vet[2]+1
		
print(vet)
		
	