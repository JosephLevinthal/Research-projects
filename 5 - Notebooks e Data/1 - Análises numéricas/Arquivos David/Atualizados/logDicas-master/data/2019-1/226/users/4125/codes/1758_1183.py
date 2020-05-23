from numpy import*
v1 = array(eval(input("digite qualquer vetor: ")))
i= 0
i1 = 0
l = 0
k = 0
while(i<size(v1)):
	if(v1[i]>=0):
		i1 = i1 + 1
	i = i + 1
a = ones(i1, dtype = int)
while(l<size(v1)):
	if(v1[l]>0):
		a[k] = v1[l]
		k = k + 1
		
	l = l +1
print(a)
	
	