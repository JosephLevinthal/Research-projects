from numpy import*
t=array(eval(input("entre com o vetor:")))

z=zeros(1,dtype=int)
a=0
for i in range(size(t)):
	if(t[i]==min(t)):
		z[a]=i
		a=a+1
print(z[0])
		