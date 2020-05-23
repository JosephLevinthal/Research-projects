from numpy import *
e= array(eval(input("digite o vetor: ")))
b = array(eval(input("digite o vetor: ")))
print(size(b))

i = 0
soma1 = 0
soma2 = 0
while(i<size(e)):
	if((e[i]==11 and b[i]==33) or (e[i]==22 and b[i]==11) or (e[i]==33 and b[i]==22)):
		soma1 = soma1 + 1
	elif((b[i]==11 and e[i]==33) or (b[i]==22 and e[i]==11) or (b[i]==33 and e[i]==22)):
		soma2 = soma2 +1
	else:
		msg = "empate"
	i = i + 1
if(soma1>soma2):
	print("EUSAPIA")
elif(soma2>soma1):
	print("BARSANULFO")
else:
	print("EMPATE")