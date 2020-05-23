from numpy import*
n= int(input("Numero de vezes: "))
i = 0
d = -2
dd = -1
x = zeros( n, dtype=int)
while (i!= size(x)):
	x[i]=x[d]+x[dd]
	x[1]=1
	i=1+i
	d=d+1
	dd=dd+1
print(x)