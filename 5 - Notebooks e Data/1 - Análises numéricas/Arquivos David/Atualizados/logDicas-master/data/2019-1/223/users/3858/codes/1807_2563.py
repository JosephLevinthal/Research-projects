from numpy import *
vetor = array(eval(input()))
ap_nm = 0
while (size(vetor) > 1):
	for x in range(size(vetor)):
		if(vetor[x]>=5 and vetor[x]<7):
			ap_nm = ap_nm + 1
	print(ap_nm)
	ap_nm = 0
	vetor = array(eval(input()))
