from numpy import*
mat=array(eval(input("digite a matriz: ")))
cont=0
for i in range (size(mat)):
	if(mat[i]%2!=0):
		cont=cont+1
x=zeros(cont, dtype=int)
p=0
for i in range (size(mat)):
	if(mat[i]%2!=0):
		x[p]=i
		p=p+1
print(cont)
print(x)
	