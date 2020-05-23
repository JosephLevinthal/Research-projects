from numpy import*
x = array(eval(input("x: ")))
y = array(eval(input("y: ")))
vet=zeros(3, dtype=int)
for i in range(size(x)):
	if x[i]>y[i]:
		vet[0]=vet[0]+1
	elif x[i]==y[i]:
		vet[1]=vet[1]+1
	elif x[i]<y[i]:
		vet[2]=vet[2]+1
print(vet)