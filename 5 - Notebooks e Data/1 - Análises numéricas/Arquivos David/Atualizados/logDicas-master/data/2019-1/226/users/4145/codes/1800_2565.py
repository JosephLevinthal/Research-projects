from numpy import*
vn=array(eval(input("vetor de notas: ")))
vp=array(eval(input("vetor de frequencia: ")))
vc=int(input("carga horaria: "))
x=zeros(3,dtype=int)
for i in range(size(vn)):
	if((vn[i]>=5)and(vp[i]>=((3/4)*vc))):
		x[0]=x[0]+1
	elif((vn[i]>=5)and(vp[i]<((3/4)*vc))):
		x[2]=x[2]+1
	elif((vn[i]<5)and(vp[i]>=((3/4)*vc))):
		x[1]=x[1]+1
		
print(x)		