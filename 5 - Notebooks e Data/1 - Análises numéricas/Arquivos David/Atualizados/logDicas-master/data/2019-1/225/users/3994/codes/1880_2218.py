from numpy import*
N = array(eval(input("Digite a matriz: ")))
g=0
for i in range(shape(N)[0]):
	for j in range(shape(N)[0]):
		if(j>i):
			g=g+N[i,j]
print(round(g,2))