from numpy import*
vet= array(eval(input("freq de alunos: ")))
ap=0

for i in range(size(vet)):
	if(vet[i]>=70):
		ap=ap+1
print(ap)
v=zeros(ap,dtype=int)
ind=0
a=0
for j in range(size(vet)):
	if(vet[j]>=70):
		vet[j]=a
		
print(a)
print(a)
	
	
	