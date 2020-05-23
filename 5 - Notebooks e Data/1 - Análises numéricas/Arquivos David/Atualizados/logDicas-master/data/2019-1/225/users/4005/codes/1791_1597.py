from numpy import*
compras=array(eval(input(":")))
s=sum(compras)
if(s>80.0):
	s=round(s-d,2)
	print(s)
elif(s<80.0):
	print(round(s,2))
