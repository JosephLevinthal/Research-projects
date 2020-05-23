from numpy import*
E = array(eval(input("jogadas de Eusapia: ")))
B = array(eval(input("jogadas de Barsanulfo: ")))

i = 0
ca = 0
cb = 0
while(i < size(E)):
	
	if(E[i] == 11) and (B[i] == 33) or (E[i]==22) and (B[i] == 11) or (E[i] == 33) and (B[i] == 22):
		ca = ca + 1
		i = i + 1
	elif(B[i] == 11) and (E[i] == 33) or (B[i] == 22) and (E[i] == 11) or (B[i] == 33) and (E[i] == 22):
		cb = cb + 1
		i = i + 1
	else:
		i = i + 1
	
print(i)
if(cb > ca):
	print("BARSANULFO")
elif(ca > cb):
	print("EUSAPIA")
else:
	print("EMPATE")