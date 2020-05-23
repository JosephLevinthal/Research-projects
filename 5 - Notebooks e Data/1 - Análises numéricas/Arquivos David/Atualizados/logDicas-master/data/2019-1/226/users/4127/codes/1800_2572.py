from numpy import*
mat= array(eval(input("vet")))
w=0
for i in range(size(mat)):
	if(mat[i]%2!=0):
		w=w+1
x=zeros(w,dtype=int)
p=0
for k in range(size(mat)):
	if(mat[k]%2!=0):
		x[p]=mat[k]
		p=p+1
print(x)