from numpy import*
x=array(eval(input("Digite os numeros de falta: ")))
n=zeros(6,dtype(float))
a=0
b=0
c=0
d=0
e=0
f=0
for i in x:
	if(i==2):
		a=a+1
	elif(i==3):
		b=b+1
	elif(i==4):
		c=c+1
	elif(i==5):
		d=d+1
	elif(i==6):
		e=e+1
	elif(i==7):
		f=f+1
n[0]=n[0]+a
n[1]=n[1]+b
n[2]=n[2]+c
n[3]=n[3]+d
n[4]=n[4]+e
n[5]=n[5]+f
h=0
for i in n:
	n[h]=(n[h]/(size(x)))*100
	n[h]=round(n[h],1)
	h=h+1
print(n)
		