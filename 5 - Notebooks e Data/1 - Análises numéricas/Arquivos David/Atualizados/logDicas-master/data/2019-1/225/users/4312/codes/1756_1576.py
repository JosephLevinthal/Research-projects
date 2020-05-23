from numpy import*
#Sequencia de jogadas de Eusápia
v1 = array(eval(input("Insira a sequencia: ")))

#Sequencia dejogadas de Barsanulfo
v2 =  array(eval(input("Insira a sequencia: ")))

i = 0
ve = 0
vb = 0

while(i < size(v1)):
	if(((v1[i]== 11) and (v2[i]==33)) or ((v1[i]==22) and (v2[i]==11)) or ((v1[i]==33) and (v2[i]==22))):
		ve = ve + 1
	elif(((v2[i]==11) and (v1[i]==33)) or ((v2[i]==22) and (v1[i]==11)) or ((v2[i]==33) and (v1[i]==22))):
		 vb = vb + 1
	i = i + 1
print(i)			  
if(ve > vb):
	print("EUSAPIA")
elif(ve < vb):
	print("BARSANULFO")
elif(ve == vb):
	print("EMPATE")
		
