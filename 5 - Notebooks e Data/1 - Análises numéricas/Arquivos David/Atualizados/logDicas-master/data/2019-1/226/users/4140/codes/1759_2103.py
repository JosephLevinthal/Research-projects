from numpy import*
va=array(eval(input()))
vb=array(eval(input()))
i=0
j=-1
while(i<size(va) and abs(j)<=size(vb)):
	if(va[i]>=vb[j]):
		print(va[i])
	else:
		print(vb[j])
	i=i+1
	j=j-1