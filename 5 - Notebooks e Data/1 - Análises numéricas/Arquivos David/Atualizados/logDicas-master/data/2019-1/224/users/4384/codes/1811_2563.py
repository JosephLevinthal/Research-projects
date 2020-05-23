from numpy import*
mf=array(eval(input("digite a media: ")))
while(size(mf)>1):
	mf=array(eval(input("digite a media: ")))
	monitor=0
	for elemento in mf:
		if(elemento>7):
			monitor=monitor+1
			print(monitor)

