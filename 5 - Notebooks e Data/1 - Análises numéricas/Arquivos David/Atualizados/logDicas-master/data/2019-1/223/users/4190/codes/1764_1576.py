from numpy import *
v1 = array(eval(input()))
v2 = array(eval(input()))
i = 0
e = 0
b = 0
while i!=size(v1):
	if ((v1[i]==11 and v2[i]==33) or (v1[i]==33 and v2[i]==22) or (v1[i]==22 and v2[i]==11)):
		e = e+1
	elif ((v2[i]==11 and v1[i]==33) or (v2[i]==33 and v1[i]==22) or (v2[i]==22 and v1[i]==11)):
		b = b+1
	elif(v1[i]==v2[i]):
		e=e+0
		b=b+0
	i = i+1
	
print(i)

if (b>e):
	print('BARSANULFO')
elif (e>b):
	print('EUSAPIA')
if (b==e):
	print('EMPATE')