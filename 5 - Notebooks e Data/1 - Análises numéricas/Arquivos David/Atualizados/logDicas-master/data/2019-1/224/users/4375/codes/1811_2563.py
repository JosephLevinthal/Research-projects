from numpy import*
finais=array(eval(input("media final: ")))
while(size(finais)>1):
	yss=0
	for i in finais:
		if(i>=5)and(i<7):
			yss=yss+1
	print(yss)
	finais=array(eval(input("media final: ")))