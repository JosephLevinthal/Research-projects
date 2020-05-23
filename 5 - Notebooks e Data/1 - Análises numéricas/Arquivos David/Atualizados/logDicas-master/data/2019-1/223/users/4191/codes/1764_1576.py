from numpy import *

e=array(eval(input("jogada da eusapia: ")))
b=array(eval(input("jogada do barsa: ")))

i=0
ve=0
vb=0
while(i<size(e)):
	if((e[i]==11)and(b[i]==33)or(e[i]==22)and(b[i]==11)or(e[i]==33)and(b[i]==22)):
		ve=ve+1
	elif(e[i]==b[i]):
		ve=ve
		vb=vb
	else:
		vb=vb+1
	i=i+1	
print(i)	

if(ve>vb):
	print('EUSAPIA')
elif(vb>ve):
	print('BARSANULFO')
elif(vb==ve):
	print('EMPATE')
			
	
	
