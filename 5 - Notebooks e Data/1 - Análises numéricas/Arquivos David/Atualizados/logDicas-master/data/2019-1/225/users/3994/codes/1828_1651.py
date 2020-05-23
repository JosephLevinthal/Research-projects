from numpy import*
vet = input("Digite o tom de pele: ").upper().split(',')
mc=0
c=0
cm=0
em=0
e=0
me=0
v = zeros(6,dtype=int)
for i in range(size(vet)):
	if(vet[i]=="MC"):
		mc=mc+1
	elif(vet[i]=="C"):
		c=c+1
	elif(vet[i]=="CM"):
		cm=cm+1
	elif(vet[i]=="EM"):
		em=em+1
	elif(vet[i]=="E"):
		e=e+1
	elif(vet[i]=="ME"):
		me=me+1
v[0]=mc
v[1]=c
v[2]=cm
v[3]=em
v[4]=e
v[5]=me
print(max(v))
print(v)
		