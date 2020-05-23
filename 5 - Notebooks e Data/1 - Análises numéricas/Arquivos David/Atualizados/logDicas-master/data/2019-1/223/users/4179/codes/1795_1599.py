from numpy import *
a=array(eval(input("Qual o custo: ")))
b=sum(a)
if (b  > 80.0):
	ct=(b-b*0.15)
	print(round(ct,2))
else:
	print(round(b,2))
	

