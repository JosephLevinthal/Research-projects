from numpy import*
vet = array(eval(input("notas: ")))
while size(vet)>1:
	nm = 0
	for x in vet:
		if (5<=x) and (x<7):
			nm = nm + 1
	print(nm)
	vet = array(eval(input("notas: ")))