from numpy import*
e=array(eval(input("digite um vetor: ")))
b=array(eval(input("digite um vetor: ")))
i=0
se=0
sb=0
ve=0
vb=0
while(i<size(e)):
	if(e[i]==11 and b[i]==11):
		ve=0
		vb=0
	elif(e[i]==22 and b[i]==22):
		ve=0
		vb=0
	elif(e[i]==33 and b[i]==33):
		ve=0
		vb=0
	elif(e[i]==11 and b[i]==22):
		ve=0
		vb=1
	elif(e[i]==11 and b[i]==33):
		ve=1
		vb=0
	elif(e[i]==22 and b[i]==11):
		ve=1
		vb=0
	elif(e[i]==22 and b[i]==33):
		ve=0
		vb=1
	elif(e[i]==33 and b[i]==11):
		ve=0
		vb=1
	elif(e[i]==33 and b[i]==22):
		ve=1
		vb=0
	se=se+ve
	sb=sb+vb
	i=i+1
print(size(e))
if(se==sb):
	print("EMPATE")
elif(se>sb):
	print("EUSAPIA")
elif(se<sb):
	print("BARSANULFO")