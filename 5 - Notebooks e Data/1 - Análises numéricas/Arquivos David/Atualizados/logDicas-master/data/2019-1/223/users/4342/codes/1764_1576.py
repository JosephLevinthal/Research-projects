from numpy import *
i=0
e=0
b=0
var=array(eval(input("vetor:")))
var1=array(eval(input("vetor:")))
while(i<size(var)):
	if((var[i]==11) and (var1[i]==33)) or ((var[i]==22) and (var1[i]==11)) or ((var[i]==33) and (var1[i]==22)):
		e=e+1
	elif((var1[i]==11) and (var[i]==33)) or ((var1[i]==22) and (var[i]==11)) or ((var1[i]==33) and (var[i]==22)):
		b=b+1
	i=i+1
print(i)
if(e>b):
	print("EUSAPIA")
elif(b>e):
	print("BARSANULFO")
else:
	print("EMPATE")
	