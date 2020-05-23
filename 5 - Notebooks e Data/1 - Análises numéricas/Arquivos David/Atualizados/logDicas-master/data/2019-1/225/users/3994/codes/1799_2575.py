from numpy import*
vet = input("Digite as opcoes: ").upper()
v=zeros(3, dtype = int)
t=0
n=0
y=0

for i in range(size(vet)):
	if(vet[i]=="TV"):
		t=t+1
	elif(vet[i] =="NETFLIX"):
		n=n+1
	elif(vet[i]=="YOUTUBE"):
		y=y+1
v[0]=t
v[1]=n
v[2]=y
print(v)
