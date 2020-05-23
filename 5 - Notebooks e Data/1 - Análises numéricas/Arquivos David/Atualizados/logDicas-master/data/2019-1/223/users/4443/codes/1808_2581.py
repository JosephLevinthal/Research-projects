from numpy import *
ve = array(eval(input("digite [tempo, admIn, admOut, ChIn, ChOut]: ")))

while(ve[0] != -1):
	admin = 0
	admout = 0
	chaoin = 0
	chaout = 0
	for i in ve:
		admin = admin + ve[1]
		admout = admout + ve[2]
		chaoin = chaoin + ve[3]
		chaout = chaout + ve[4]
	ve = array(eval(input("digite [tempo, admIn, admOut, ChIn, ChOut]: ")))	
print("ADM")

print("Entrada: ",admin)
print("Saida: ",admout)
print("CHAO")
print("Entrada: ",chaoin)
print("Saida: ",chaout)

		