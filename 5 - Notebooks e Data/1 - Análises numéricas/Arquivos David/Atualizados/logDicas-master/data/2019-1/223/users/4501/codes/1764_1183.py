from numpy import*
v=array(eval(input("vetor: ")))
i=0
z=0
while(i<len(v)):
	if(v[i]>=0):
		z=z+1
	i=i+1
z=z
pe=0
ps=0
vs=zeros(z, dtype=int)
while(pe<size(v)):
	if(v[pe]>=0):
		vs[ps]=v[pe]
		pe=pe+1
		ps=ps+1
	else:
		pe=pe+1
		ps=ps
print(vs)		