from numpy import*
v1= array(eval(input("qual seu vetor 1? ")))
v2= array(eval(input("qual seu vetor 2? ")))

i=0
e=0
b=0

while (i<size(v1) and size(v2)):
	if(v1[i]==11 and v2[i]==22):
		b= b+1
	elif(v1[i]==22 and v2[i]==11):
		e=e+1
	elif(v1[i]==11 and v2[i]==33):
		e=e+1
	elif(v1[i]==33 and v2[i]==11):
		b=b+1
	elif(v1[i]==22 and v2[i]==33):
		b= b+1
	elif(v1[i]==33 and v2[i]==22):
		e=e+1
	i= i+1
if(b>e):
	print(i)
	print("BARSANULFO")
	
elif(b<e):
	print(i)
	print("EUSAPIA")
else:
	print(i)
	print("EMPATE")
	