from numpy import*
me=array(eval(input("medias: ")))
p=array(eval(input("num. de horas: ")))
ch=int(input("carga horaria: "))
x=zeros(3,dtype=int)
for i in range(size(me)):
	if(me[i]>=5 and p[i]>=((ch*75)/100)):
		x[0]=x[0]+1
	elif(me[i]<5 and p[i]>((ch*75)/100)):
		x[1]=x[1]+1
	elif(me[i]>=5 and p[i]<((ch*75)/100)):
		x[2]=x[2]+1
print(x)
	
