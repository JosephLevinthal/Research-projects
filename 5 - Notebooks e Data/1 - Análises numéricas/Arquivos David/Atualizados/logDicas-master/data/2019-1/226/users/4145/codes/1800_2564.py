from numpy import*
x=zeros(3,dtype=int)
vd=array(eval(input("vetor de gols dados: ")))
vl=array(eval(input("vetor de gols levados: ")))
for i in range(size(vd)):
	if(vd[i]==vl[i]):
		x[1]=x[1]+1
	elif(vd[i]<vl[i]):	
		x[2]=x[2]+1
	elif(vd[i]>vl[i]):
		x[0]=x[0]+1

print(x)
	