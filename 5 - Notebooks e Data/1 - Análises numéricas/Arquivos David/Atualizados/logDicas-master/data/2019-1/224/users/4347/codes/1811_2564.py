from numpy import*
x=array(eval(input("tabela 1: ")))
y=array(eval(input("tabela 2: ")))
m=zeros(3,dtype=int)
h=0
j=0
t=0
g=0
for i in x:
	if(i > y[h]):
		j=j+1
		h=h+1
	elif (i ==y[h]):
		t=t+1
		h=h+1
	elif (i < y[h]):
		g=g+1
		h=h+1
m[0]=m[0]+j
m[1]=m[1]+t
m[2]=m[2]+g
print (m)

	   