from numpy import *
v1 = array(eval(input("Digite v1: ")))
v2 = array(eval(input("Digite v2: ")))
print(size(v1))
i =0
cont1=0
cont2=0
while(i<size(v1)):
	if(v1[i]==11 and v2[i]==33)or(v1[i]==22 and v2[i]==11)or(v1[i]==33 and v2[i]==22):
		cont1=cont1+1
	elif((v2[i]==11 and v1[i]==33)or(v2[i]==22 and v1[i]==11)or(v2[i]==33 and v1[i]==22)):
		cont2=cont2+1
	else:
		msg="EMPATE"
	i=i+1
if(cont1>cont2):
	print("EUSAPIA")
elif(cont2>cont1):
	print("BARSANULFO")
else:
	print("EMPATE")