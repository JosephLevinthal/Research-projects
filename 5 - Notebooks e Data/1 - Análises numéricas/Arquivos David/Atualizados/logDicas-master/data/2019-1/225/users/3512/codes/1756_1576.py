from numpy import*

vetor1= array(eval(input("elemetary eusapia: "))) #iram ser corrspodntes das cont 1 e 2 
vetor2= array(eval(input("elemetary barsa: ")))

cont=0
cont1=0
cont2= 0

pedra= 11
papel=22
tesoura=33


while(cont < size(vetor1)):
	if (vetor1[cont] == pedra and vetor2[cont] == papel):
		cont1 = cont1 + 1
	elif(vetor1[cont] == papel and vetor2[cont]== tesoura):
		cont1= cont1 + 1
	elif (vetor1[cont] == tesoura and vetor2[cont] == pedra):
		cont1= cont1 + 1
	elif(vetor1[cont] != vetor2[cont]):
		cont2= cont2 + 1
	cont = cont + 1
	
print(size(vetor1))
