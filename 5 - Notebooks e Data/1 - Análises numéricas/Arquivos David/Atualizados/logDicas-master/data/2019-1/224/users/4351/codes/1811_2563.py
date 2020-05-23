from numpy import*
mf=array(eval(input("vetor de notas finais: ")))

while (size(mf)>1):
	i=0
	apr=0
	for v in mf:
		if (mf[i]>=5 and mf[i]<7):
			apr= apr + 1
			i= i + 1
		else:
			i = i + 1
	
	print(apr)
	mf=array(eval(input("vetor de notas finais: ")))
	
			