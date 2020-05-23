from numpy import *
m=array(eval(input("medias: ")))
h=array(eval(input("horas: ")))
cg=float(input("carga horaria: "))
v= zeros(3, dtype=int)
a=0
b=0
c=0
y=0
for x in m:
	if(x>=5)and(h[y]>=cg*0.75):
		a+=1
	elif(x<5)and(h[y]>cg*0.75):
		b+=1
	elif (h[y]<cg*0.75):
		c+=1
	y+=1
v[0]=a
v[1]=b
v[2]=c
print(v)