from numpy import*
n=array(eval(input("saques: ")))
cont=0
for i in range (size(n)):
	if(n[i]>=2000):
		cont=cont+1
x=zeros(cont, dtype=int)
p=0
for i in range (size(n)):
	if(n[i]>=2000):
		x[p]=i
		p=p+1
print(cont)
print(x)
	