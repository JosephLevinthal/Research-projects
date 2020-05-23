from numpy import*
v1=array(eval(input("Jogadas eusapia: ")))
v2=array(eval(input("Jogadas barsanulfo: ")))
i=0#contadora
a=0#e
b=0#b
while(i<size(v1)):
	if(v1[i]==11 and v2[i]==33):
		a=a+1
	elif(v1[i]==11 and v2[i]==22):
		b=b+1
	elif(v1[i]==22 and v2[i]==11):
		a=a+1
	elif(v1[i]==22 and v2[i]==33):
		b=b+1
	elif(v1[i]==33 and v2[i]==11):
		b=b+1
	elif(v1[i]==33 and v2[i]==22):
		a=a+1
	i=i+1
print(i)
if(a>b):
	print("EUSAPIA")
elif(a<b):
	print("BARSANULFO")
else:
		print("EMPATE")
	