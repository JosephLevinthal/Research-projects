from numpy import*
f= array(eval(input("insira as faltas: ")))
z= zeros(6, dtype=float)
q=size(f)
for i in f:
	if i==2:
		z[0]=z[0]+1
	elif i==3:
		z[1]=z[1]+1
	elif i==4:
		z[2]=z[2]+1
	elif i==5:
		z[3]=z[3]+1
	elif i==6:
		z[4]=z[4]+1
	elif i==7:
		z[5]=z[5]+1
for l in range(size(z)):
	z[l]=round((z[l]*100)/size(f),1)
print(z)

	