from numpy import*
x=array(eval(input("Digite os pacientes: ")))
j=0
g=0
while(size(x)>j):
	if(x[j]>99):
		print(j)
		j=j+1
		g=g+1
	else:
		j=j+1
print(g)		