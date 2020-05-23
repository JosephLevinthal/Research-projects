from numpy import*
x=int(input("Digite um numero inteiro: "))
z=zeros((x,x),dtype=int)
for i in range(0,x):
	for j in range(0,x):
		z[i,j]=min(i,j)+1
print(z)		
	 