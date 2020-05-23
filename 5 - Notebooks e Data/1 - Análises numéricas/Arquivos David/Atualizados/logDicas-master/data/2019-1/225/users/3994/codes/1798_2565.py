from numpy import*
vet1= array(eval(input("Medias finais: ")))
vet2= array(eval(input("Presenca:")))
ch= int(input("Carga horaria:"))
ap=0
rn=0
rf=0

v = zeros(3, dtype=int)

for i in range(size(vet1)):
	y = ch*75/100
	if(vet1[i]>=5 and vet2[i]>=y):
		ap = ap+1
	elif(vet1[i]<5):
		rn = rn+1
	elif(vet2[i]<y):
		rf = rf+1
v[0]=ap
v[1]=rn
v[2]=rf
print(v)
		
		
