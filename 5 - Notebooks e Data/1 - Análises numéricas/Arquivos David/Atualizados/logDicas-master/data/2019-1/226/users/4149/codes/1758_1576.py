from numpy import*

e=array(eval(input("entre com o vetor da eusapia:")))
b=array(eval(input("entre com o vetor da barsanulfo:")))

print(size(e))

i=0
ve=0
vb=0

while(i<size(e)):
	if((e[i]==11 and b[i]==33) or (e[i]==22 and b[i]==11) or (e[i]==33 and b[i]==22)):
		ve=ve+1
	elif((e[i]==33 and b[i]==11) or (e[i]==11 and b[i]==22) or (e[i]==22 and b[i]==33)):
		vb=vb+1
	i=i+1
if(ve>vb):
	print("EUSAPIA")
elif(vb>ve):
	print("BARSANULFO")
elif(ve==vb):
	print("EMPATE")