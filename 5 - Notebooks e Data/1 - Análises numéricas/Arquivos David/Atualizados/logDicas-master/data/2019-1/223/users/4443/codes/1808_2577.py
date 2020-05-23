from numpy import *
frase = input("Digite uma frase: ")
frase = frase.lower()

for i in frase:
	if(i == "a"):
		frase = frase.replace("a","")
	elif(i== "e"):	
		frase = frase.replace("e","")
	elif(i == "i"):
		frase = frase.replace("i","")
	elif(i == "o"):
		frase = frase.replace("o","")
	elif(i == "u"):	
		frase = frase.replace("u","")
print(frase)