from numpy import*
bilu=array(eval(input("vetor bilu: ")))


while size(bilu)>1 :
	i=0
	par=0
	impar=0
	for v in bilu:
		if (bilu[i]%2==0):
			par= par + 1
			i= i + 1
		else:
			impar = impar + 1
			i= i + 1
	print(par)
	print(impar)
	print(size(bilu))
	bilu=array(eval(input("vetor bilu: ")))
	