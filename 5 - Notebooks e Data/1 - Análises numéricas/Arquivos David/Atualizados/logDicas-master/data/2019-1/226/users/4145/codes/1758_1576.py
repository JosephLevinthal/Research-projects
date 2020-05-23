from numpy import*
je = array(eval(input("jogadas de eusapia: ")))
jb = array(eval(input("jogadas de basarnulfo: ")))
i=0
ve=0
vb=0
while(i<size(je) and size(je)==size(jb)):
	if((je[i]==11 and jb[i]==33)or(je[i]==22 and jb[i]==11 )or(je[i]==33 and jb[i]==22)):
		i = i+1
		ve= ve+1
	elif((jb[i]==11 and je[i]==33)or(jb[i]==22 and je[i]==11 )or(jb[i]==33 and je[i]==22)):	
		i = i +1
		vb =vb +1
	else:
		i = i+1
print(i)
if(ve>vb):
	print("EUSAPIA")
elif(vb>ve):
	print("BARSANULFO")
else:
	print("EMPATE")
	