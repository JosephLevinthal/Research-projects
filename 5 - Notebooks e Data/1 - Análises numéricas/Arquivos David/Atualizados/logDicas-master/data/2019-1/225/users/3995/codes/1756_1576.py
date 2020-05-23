from numpy import*
v1=array(eval(input("jogadas de Eusapia:")))
v2=array(eval(input("jogadas de Barsanulfo:")))
i=0
E=0
B=0
while(i<size(v1)):  #v1 e v2 terao a mesma quantidade de termos.
	if(v1[i]!=v2[i]):
		if((v1[i]==11 and v2[i]==33)or(v1[i]==22 and v2[i]==11)or(v1[i]==33 and v2[i]==22)):
			E=E+1
		elif((v2[i]==11 and v1[i]==33)or(v2[i]==22 and v1[i]==11)or(v2[i]==33 and v1[i]==22)):
			B=B+1
	else:
		E=E+0
		B=B+0
	i=i+1
if(E>B):
	msg="EUSAPIA"
elif(B>E):
	msg="BARSANULFO"
else:
	msg="EMPATE"
print(size(v2))
print(msg)