from numpy import*
e=array(eval(input("jogadas de Eusapia: ")))
b=array(eval(input("jogadas de Baesanulgo: ")))

co=0
ce=0
cb=0
while(co!=size(e)):
	if(e[co]==b[co]):
		ce+=0
		cb+=0
	if(e[co]==11)and(b[co]==22)or(e[co]==22)and(b[co]==33)or(e[co]==33)and(b[co]==11):
		cb+=1
	if(e[co]==11)and(b[co]==33)or(e[co]==22)and(b[co]==11)or(e[co]==33)and(b[co]==22):
		ce+=1
	co+=1
print(co)
if(ce>cb):
	print("EUSAPIA")
elif(cb>ce):
	print("BARSANULFO")
if(ce==cb):
	print("EMPATE")