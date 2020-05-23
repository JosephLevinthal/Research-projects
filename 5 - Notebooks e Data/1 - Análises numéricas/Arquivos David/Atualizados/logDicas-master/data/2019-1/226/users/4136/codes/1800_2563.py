from numpy import*
v = array(eval(input("notas: ")))
while(size(v)>1):
	aprovado = 0
	for e in v:
		if(e>=5 and e<7):
			aprovado = aprovado + 1
	print(aprovado)
	v = array(eval(input("vetor2: ")))