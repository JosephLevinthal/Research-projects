from numpy import*
mf = array(eval(input("Media final: ")))


while(size(mf) > 1):
	ap = 0
	
	for i in range(size(mf)):
		if(mf[i] >= 5 and mf[i] < 7):
			ap = ap + 1
	print(ap)
	mf = array(eval(input("Media final: ")))

