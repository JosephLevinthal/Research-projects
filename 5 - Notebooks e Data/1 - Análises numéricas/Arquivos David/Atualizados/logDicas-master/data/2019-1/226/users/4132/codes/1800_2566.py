from numpy import *
v = array(eval(input("Digite: ")))

x = zeros(6,dtype=float)
aux = array([2.0,3.0,4.0,5.0,6.0,7.0])
acum=0

for i in range(size(aux)):
	for j in range(size(v)):
		if(float(v[j])==aux[i]):
			acum+=1
	acum = acum*100/size(v)
	x[i]=float(acum)
	acum=0
x[0]= round(x[0],1)
x[1]= round(x[1],1)
x[2]= round(x[2],1)
x[3]= round(x[3],1)
x[4]= round(x[4],1)
x[5]= round(x[5],1)
print(x)