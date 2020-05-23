from numpy import*
x=array(eval(input("Digite as notas: ")))
y=array(eval(input("Digite as frequencias: ")))
z=int(input("Digite a carga horaria: "))
z=z*0.75
h=0
t=0
l=0
p=0
for i in x:
	if(i >=5 )and (y[h] >= z):
		t=t+1
		h=h+1
	elif(i >=5 ) and (y[h] < z):
		l=l+1
		h=h+1
	elif(i < 5) and (y[h] >= z):
		p=p+1
		h=h+1
m=zeros(3,dtype(int))
m[0]=m[0]+t
m[1]=m[1]+p
m[2]=m[2]+l
print(m)