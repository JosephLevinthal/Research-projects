from numpy import *
v1 = array(eval(input()))
v2 = array(eval(input()))
i = 0
e=0
b=0
while(i<size(v1)):
	if(v1[i]==11 and v2[i]==33):
		b=b+1
	elif(v1[i]==22 and v2[i]==11):
		b=b+1
	elif(v1[i]==33 and v2[i]==22):
		b=b+1
	elif(v2[i]==11 and v1[i]==33):
		e=e+1
	elif(v2[i]==22 and v1[i]==11):
		e=e+1
	elif(v2[i]==33 and v1[i]==22):
		e=e+1
		
	
	i=i+1
if(e>b):
	m = "EUSAPIA"
elif(e<b):
	m = "BARSANULFO"
else:
	m = "EMPATE"
	
print(i)
print(m)