from numpy import*
#entradas: 11=pedra, 22=papel, 33=tesoura
e= array(eval(input("sequencia de eusapia: ")))
b= array(eval(input("sequencia de barsanulfo: ")))
i=0
ce=0
cb=0

while(i<size(e)):
	if((e[i]==11)and(b[i]==22)):
		cb=cb+1
	elif((e[i]==11)and(b[i]==33)):
		ce=ce+1
	elif((e[i]==22)and(b[i]==11)):
		ce=ce+1
	elif((e[i]==22)and(b[i]==33)):
		cb=cb+1
	elif((e[i]==33)and(b[i]==11)):
		cb=cb+1
	elif((e[i]==33)and(b[i]==22)):
		ce=ce+1
	elif(e[i]==b[i]):
		ce=ce+0
		cb=cb+0
	i=i+1	
print(size(e))
if(ce>cb):
	print("EUSAPIA")
elif(cb>ce):
	print("BARSANULFO")
else:
	print("EMPATE")
	
	

