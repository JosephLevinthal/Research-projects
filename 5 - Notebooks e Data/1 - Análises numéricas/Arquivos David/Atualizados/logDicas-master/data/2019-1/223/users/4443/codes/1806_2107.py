from numpy import *
ve = input("Digite uma palavra: ")
ve = ve.lower()
vogais = 0
j = 0
while(j < len(ve)):
	if(ve[j] == "a" or ve[j] == "e" or ve[j] == "i" or ve[j] == "o" or ve[j] == "u"):
		vogais = vogais + 1
	j = j+1
print(vogais)		
print(len(ve) - vogais)