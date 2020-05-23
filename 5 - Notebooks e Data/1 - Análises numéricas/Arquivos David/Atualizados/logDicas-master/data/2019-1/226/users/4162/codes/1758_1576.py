from numpy import*
v= array(eval(input("digite um vetor: ")))
v1= array(eval(input("digite um vetor: ")))
t= size(v)
s=0
cv=0
cv1=0
a=v[cv]
b=v1[cv1]
ve=0 
vb=0
while s!=t:
	a=v[cv]
	b=v1[cv1]
	if a==11 and b==22:
		ve=ve+0
		vb=vb+1
	elif a==11 and b==33:
		ve=ve+1
		vb=vb+0
	elif a==22 and b==11:
		ve=ve+1
		vb=vb+0
	elif a==22 and b==33:
		ve=ve+0
		vb=vb+1
	elif a==33 and b==11:
		ve=ve+0
		vb=vb+1
	elif a==33 and b==22:
		ve=ve+1
		vb=vb+0
	else:
		ve=ve+0
		vb=vb+0
	cv=cv+1
	cv1=cv1+1
	s=s+1
if ve>vb:
	print(t)
	print("EUSAPIA")
elif ve<vb:
	print(t)
	print("BARSANULFO")
elif ve==vb:
	print(t)
	print("EMPATE")