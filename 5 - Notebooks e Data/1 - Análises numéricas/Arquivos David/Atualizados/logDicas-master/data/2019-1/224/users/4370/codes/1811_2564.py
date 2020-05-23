from numpy import *
vg1=array(eval(input("gols da partida: ")))
vg2=array(eval(input("gols do time adversario: ")))
v= vg1-vg2
vi=0
em=0
de=0
for pos in v:
	if(pos==0):
		em= em+1
	elif(pos > 0):
		vi= vi+1
	else:
		de= de+1
z=zeros(3,dtype=int)
z[0] = vi
z[1]= em
z[2]= de
print(z)
