from numpy import*

vet = array(eval(input("Digite as notas: ")))


while	(size(vet) > 1):
	nota = 0
	
	for elemento in vet:
		if	(elemento >= 5 and elemento < 7):
			
			nota = nota + 1
			
	print(nota)
	
	vet = array(eval(input("Digite as notas:")))