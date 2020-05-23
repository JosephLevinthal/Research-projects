from numpy import *
string = input("digite a string: ")
string = string.upper()
i = 0
vogal = 0
consoante = 0
while(i < len(string)):
	if(string[i] == "A"):
		vogal = vogal + 1
	elif(string[i] == "E"):
		vogal = vogal + 1
	elif(string[i] == "I"):
		vogal = vogal + 1
	elif(string[i] == "O"):
		vogal = vogal + 1
	elif(string[i] == "U"):
		vogal = vogal + 1
	else:
		consoante  = consoante + 1
	i = i + 1
print(vogal)
print(consoante)
