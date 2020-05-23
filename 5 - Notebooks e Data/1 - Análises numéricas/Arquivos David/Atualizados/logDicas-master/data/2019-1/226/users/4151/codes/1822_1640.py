from numpy import*
a=array(eval(input("quantidade de alunos matriculado: ")))
impar=0
for i in range(size(a)):
	if(a[i]%2!=0):
		impar=impar+1
print(impar)

k=0
x=zeros(impar, dtype=int)
for i in range(size(a)):
	if(a[i]%2!=0):
		x[k]=i
		k=k+1
print(x)
	