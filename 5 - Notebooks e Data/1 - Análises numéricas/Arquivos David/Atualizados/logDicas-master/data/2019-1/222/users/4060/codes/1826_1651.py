from numpy import*
pele=input("pele: ").split(',')
mc=0
c=0
cm=0
em=0
e=0
me=0
aux=0
v_zeros=zeros(6, dtype=int)
for i in pele:
	if(i=="MC"):
		mc=mc+1
		v_zeros[0]=v_zeros[0]+1
	elif(i=="C"):
		c=c+1
		v_zeros[1]=v_zeros[1]+1
	elif(i=="CM"):
		cm=cm+1
		v_zeros[2]=v_zeros[2]+1
	elif(i=="EM"):
		em=em+1
		v_zeros[3]=v_zeros[3]+1
	elif(i=="E"):
		e=e+1
		v_zeros[4]=v_zeros[4]+1
	elif(i=="ME"):
		me=me+1
		v_zeros[5]=v_zeros[5]+1
print(max(mc,c,cm,em,e,me))	
print(v_zeros)