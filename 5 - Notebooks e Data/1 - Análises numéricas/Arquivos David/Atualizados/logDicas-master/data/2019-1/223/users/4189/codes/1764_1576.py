from numpy import *
E = array(eval(input("eusapia:")))
B = array(eval(input("barsanulfo:")))
ve = 0
vb = 0 
vetor = 0
while(vetor<size(E)):
	if((E[vetor]==11)and(B[vetor]==22)):
		vb=vb+1
	elif((E[vetor]==11)and(B[vetor]==33)):
		ve=ve+1
	elif((E[vetor]==22)and(B[vetor]==33)):
		vb=vb+1
	elif((E[vetor]==22)and(B[vetor]==11)):
		ve=ve+1
	elif((E[vetor]==33)and(B[vetor]==22)):
		ve=ve+1
	elif((E[vetor]==33)and(B[vetor]==11)):
		vb=vb+1
	
	vetor=vetor+1
print(size(E))
	
if(ve>vb):
	print("EUSAPIA")
elif(vb>ve):
	print("BARSANULFO")
elif(vb==ve):
	print("EMPATE")