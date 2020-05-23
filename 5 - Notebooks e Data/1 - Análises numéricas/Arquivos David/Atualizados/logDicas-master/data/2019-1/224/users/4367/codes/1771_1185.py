from numpy import*
g=array(eval(input("escreva um vetor de n elementos: ")))
i=0
no=0
while(i<size(g)):
	if(g[i]>99):
		print(i)
		no=no+1
	i=i+1
print(no)
	