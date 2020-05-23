from numpy import*
n = int(input("dIMENSaO DA MATRIZ: "))
mat =ones((n,n), dtype=int)

for x in range(n):
	for y in range (n):
		if (x<y):
			mat[x,y]= x+1
		elif (y>x):
			mat[x,y]=y+1
		else:
			mat[x,y]=y+1
print(mat)