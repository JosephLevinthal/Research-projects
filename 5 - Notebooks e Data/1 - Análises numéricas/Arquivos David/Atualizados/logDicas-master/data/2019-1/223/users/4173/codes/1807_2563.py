from numpy import*
vet = array(eval(input()))

while size(vet) > 1:
	a = 0
	for b in vet:
		if b >= 5 and b < 7:
			a += 1
	print(a)
	vet = array(eval(input()))