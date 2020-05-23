from numpy import*
n=array(eval(input("vetor de notas: ")))
r=0
al=size(n)
for i in range(al):
	if (n[i]<5):
		r= r + 1
rp=zeros(r,dtype=int)
c=0
for i in range(al):
	if (n[i]<5):
		rp[c]=i
		c= c + 1
print(r)
print(rp)
		
