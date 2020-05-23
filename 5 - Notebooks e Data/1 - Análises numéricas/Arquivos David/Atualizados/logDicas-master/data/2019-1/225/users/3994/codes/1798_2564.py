from numpy import*
vet1= array(eval(input("Digite gols do time: ")))
vet2= array(eval(input("Digite gols adversario: ")))
nv=0
ne=0
nd=0
v = zeros(3, dtype=int)

for i in range(size(vet1)):
	if(vet1[i]>vet2[i]):
		nv= nv+1
	elif(vet1[i]==vet2[i]):
		ne= ne+1
	elif(vet1[i]<vet2[i]):
		nd = nd+1
v[0]= nv
v[1]= ne
v[2]= nd
print(v)
		
		


