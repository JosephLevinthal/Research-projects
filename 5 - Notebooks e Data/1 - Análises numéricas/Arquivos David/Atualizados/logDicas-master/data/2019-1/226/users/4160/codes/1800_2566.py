from numpy import *
f = array(eval(input("Faltas: ")))
v = zeros(6,dtype=int)

for i in range(size(f)):
	if f[i]==2:
		v[0] = v[0] + 1 
	if f[i]==3:
		v[1] = v[1] + 1 
	if f[i]==4:
		v[2] = v[2] + 1 
	if f[i]==5:
		v[3] = v[3] + 1
	if f[i]==6:
		v[4] = v[4] + 1 
	if f[i]==7:
		v[5] = v[5] + 1 
y = (v/size(f))*100
for j in range(size(v)):
	y[0]= round(y[0],1)
	y[1]= round(y[1],1)
	y[2]= round(y[2],1)
	y[3]= round(y[3],1)
	y[4]= round(y[4],1)
	y[5]= round(y[5],1)
print(y)
	