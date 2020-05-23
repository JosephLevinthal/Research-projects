from numpy import*
ve=array(eval(input("vetor: ")))
vb=array(eval(input("vertor: ")))
i=0
somave=0
somab=0
somae=0

print(size(ve))

while(i<size(ve)):
	if(ve[i]==11 and vb[i]==33 or ve[i]==22 and vb[i]==11 or ve[i]==33 and vb[i]==22):
		somave=somave+1
		
	elif(vb[i]==11 and ve[i]==33 or vb[i]==22 and ve[i]==11 or vb[i]==33 and ve[i]==22):
		somab=somab+1
	i=i+1

if(somave>somab):
	print("EUSAPIA")
elif(somave<somab):
	print("BARSANULFO")
else:
	print("EMPATE")
		
		
		
	
	
