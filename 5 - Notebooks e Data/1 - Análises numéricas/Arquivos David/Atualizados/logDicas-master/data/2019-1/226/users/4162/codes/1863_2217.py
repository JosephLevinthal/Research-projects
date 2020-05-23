from numpy import*
mt=array(eval(input("insira a matriz quadrada: ")))
q=shape(mt)[0]
r=(q**2-q)//2
v=zeros(r,dtype=float)
s=0
for i in range(q):
	for j in range(q):
		if i>j:
			v[s]=mt[i,j]
			s=s+1
print(min(v))