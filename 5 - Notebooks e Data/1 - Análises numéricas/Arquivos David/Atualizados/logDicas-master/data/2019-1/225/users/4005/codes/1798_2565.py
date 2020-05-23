from numpy import*
m=array(eval(input("medias:")))
p=array(eval(input("presença:")))
v3=int(input("carga horaria:"))
ap=0
rf=0
rn=0

v=zeros(3, dtype=int)
for i in range(size(m)):
	y=v3*75/100
	if(m[i]>=5 and p[i]>=y):
		ap+=1
	elif(m[i]<5):
		rn=rn+1
	elif(p[i]<y):
		rf=rf+1
v[0]=ap
v[1]=rn
v[2]=rf
print(v)