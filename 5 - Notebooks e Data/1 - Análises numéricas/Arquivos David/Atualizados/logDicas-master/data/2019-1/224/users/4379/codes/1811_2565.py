from numpy import *
mf=array(eval(input("digite o vetor: ")))
pres=array(eval(input("digite as frequencias: ")))
carga=int(input("digites a carga horaria: "))
a=0
rn=0
rf=0
for x,y in zip(mf,pres):
	
	if(x>= 5 and y>= (75/100)*carga):
		a=a+1
	if(x<5):
		rn=rn+1
	if(y<(75/100)*carga):
		rf=rf+1
z=zeros(3,dtype=int)
z[0]=a
z[1]=rn
z[2]=rf
print(z)
		

