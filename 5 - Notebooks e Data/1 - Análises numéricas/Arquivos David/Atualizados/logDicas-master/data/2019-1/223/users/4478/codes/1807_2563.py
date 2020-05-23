from numpy import*
notas = array(eval(input("nota final: ")))

while(size(notas) > 1):
	aprovados = 0
	for x in notas:
		if(x>=5 and x<7):
			aprovados = aprovados + 1

	print (aprovados)
	notas = array(eval(input("nota final: ")))