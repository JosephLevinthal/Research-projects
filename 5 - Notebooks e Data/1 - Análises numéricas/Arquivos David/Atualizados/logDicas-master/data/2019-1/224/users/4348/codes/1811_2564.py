from numpy import*
vet1 = array(eval(input("Time casa:")))
vet2 = array(eval(input("Time fora:")))
v = 0 
i=0
g =0
e = 0
d = 0
a = zeros(3, dtype=int)
while (i<size(vet1)):
	while ( size(vet1)>g):
		if (vet1[i]>vet2[g]):
			v+=1
		elif (vet1[i]==vet2[g]):
			e+=1
		else:
			d+=1
		g+=1
		i+=1	
a[0] = v
a[1] = e
a[2]= d
print(a)