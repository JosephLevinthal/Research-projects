from numpy import*
t = array(eval(input("Digite o tempo: ")))
m = array(eval(input("Digite o modo: "))).upper()
i=0
b=0 #quente
b1=0 
c=0 #morno
c1=0
d=0 #frio
d1=0
while(i<size(t)):
	if(m[i]=="QUENTE"):
		b=b+1
		b1=90*0.005
	elif(m[i]=="MORNO"):
		c=c+1
		c1=45*0.005
	elif(m[i]=="FRIO"):
		d=d+1
		d1=0*0.005
	i=i+1
	k = sum(i)
print(round(k,2))