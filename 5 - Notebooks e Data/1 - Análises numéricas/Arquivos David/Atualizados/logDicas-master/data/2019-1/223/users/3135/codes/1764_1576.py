from numpy import*

e= array(eval(input("Insira a sequencia de jogadas de Eusapia: ")))
b= array(eval(input("Insira a sequencia de jogadas de Barsanulfo: ")))

i=0
ev= 0
bv= 0 

while (i<size(e) and i<size(b)):
	if (e[i]==11 and b[i]==11): #EMPATE/PEDRAS
		ev= ev + 1 
		bv= bv + 1
	elif (e[i]==11 and b[i]==22): #PEDRA X PAPEL
		bv= bv + 1
	elif (e[i]==11 and b[i]==33): #PEDRA X TESOURA
		ev= ev + 1
	
	elif (e[i]==22 and b[i]==22): #EMPATE/PAPEIS
		ev= ev + 1 
		bv= bv + 1
	elif (e[i]==22 and b[i]==33): #PAPEL X TESOURA
		bv= bv + 1
	elif (e[i]==22 and b[i]==11): #PEDRA X PAPEL
		ev= ev + 1
	
	elif(e[i]==33 and b[i]==33): #EMPATE/TESOURAS
		ev= ev + 1 
		bv= bv + 1
	elif(e[i]==33 and b[i]==11): #TESOURA X PEDRA
		bv= bv+1
	elif(e[i]==33 and b[i]==22): #TESOURA X PAPEL
		ev= ev + 1
	i+=1
print(i)
if (bv > ev):
	print("BARSANULFO")
elif (ev > bv):
	print("EUSAPIA")
else:
	print("EMPATE")