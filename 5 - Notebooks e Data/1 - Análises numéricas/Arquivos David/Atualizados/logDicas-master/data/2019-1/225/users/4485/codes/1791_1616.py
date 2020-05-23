from numpy import*

magia=input("magia(as):")
dano=  array(eval(input("nivel:")))
i=0
l=0
p=0
r=0
k=0
f=0

if(magia == "GELO"):
	l = dano * 2
elif(magia == "FOGO"):
	p = dano * 3
elif(magia == "CHOQUE"):
	r = dano * 4
elif(magia == "CONJURACAO"):
	k = dano*8
elif(magia == "ILUSAO"):
	f = dano*10
	
print(l+p+r+k+f)