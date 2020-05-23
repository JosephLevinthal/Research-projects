from numpy import *
e = array(eval(input("num:")))
b = array(eval(input("num:")))
pedra = 11
papel = 22
tesoura = 33
ve = 0
bar = 0
eu = 0
while(ve < size(e)):
	if(e[ve] == tesoura and b[ve] == pedra):
		bar = bar + 1
	elif((e[ve] == tesoura and b[ve] == papel)):
		eu = eu + 1
	elif(e[ve] == papel and b[ve] == tesoura):
		bar = bar + 1
	elif(e[ve] == papel and b[ve] == pedra):
		eu = eu + 1 
	elif(e[ve] == pedra and b[ve] == tesoura):
		eu = eu + 1
	elif(e[ve] == pedra and b[ve] == papel):
		bar = bar + 1	
	ve = ve + 1 
print(size(e))
if(eu > bar):
	print("EUSAPIA")
elif(eu<bar):
	print("BARSANULFO")
else:
	print ("EMPATE")