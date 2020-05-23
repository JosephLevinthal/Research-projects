from numpy import*

mat=array(eval(input("enjfn:")))
l=shape(mat)[0]
c=shape(mat)[1]
t=0
for i in range(l):
	for j in range(c):
		if(i<j):
			t=t+mat[i,j]

print(round(t,2))