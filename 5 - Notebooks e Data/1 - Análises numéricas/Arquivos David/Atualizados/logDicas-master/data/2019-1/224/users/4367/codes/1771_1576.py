from numpy import*
e=array(eval(input("digite um vetor: ")))
b=array(eval(input("digite um vetor: ")))
e1=size(e)
b1=size(b)
i=0
ve=0
vb=0
while(i<e1 and i<b1):
	i=i+1
	if(e==11 and b==33) or (e==22 and b==11) or (e==33 and b==22):
		ve=ve+1
	elif(b==11 and e==33) or (b==22 and e==11) or (b==33 and e==22):
		vb=vb+1
	elif(b==11 and e==11) or (b==22 and e==22) or (b==33 and e==33) :
		vb=vb
		ve=ve
print(i)
print()