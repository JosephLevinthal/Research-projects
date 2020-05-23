from numpy import*
m=array(eval(input(" matriculas: ")))
n=0
#x=zeros(n,dtype=int)
for i in range (size(m)):
	if(m[i]%2!=0):
		n=n+1
x=zeros(n,dtype=int)
j=0
for k in range(size(m)):
	if(m[k]%2!=0):
		x[j]= m[k]
		j=j+1
print(x)


