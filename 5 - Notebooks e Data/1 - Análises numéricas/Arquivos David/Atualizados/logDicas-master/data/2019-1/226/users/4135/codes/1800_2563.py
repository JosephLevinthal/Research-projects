from numpy import*
vet = array(eval(input("Digite a media final: ")))
while size(vet)>[1]:
	#numero de monitor
	n=0
	for x in vet:
		if 5<=x<7:
			n = n+1
	print(n)
	vet = array(eval(input("Digite a media final: ")))

	
	