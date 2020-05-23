from numpy import*
mf=array(eval(input("escreva as medias finais: ")))

while(size(mf)>1):
	ap=0
	for i in mf:
		if(i>=5) and (i<7):
			ap=ap+1
	print(ap)
	mf=array(eval(input("escreva as medias finais: ")))