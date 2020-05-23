from numpy import *
ve = input("Digite uma palavra: ")
ve = ve.lower()
i=0
for i in range(len(ve)):
	if(ve[i] != "a" and ve[i] != "e" and ve[i] != "i" and ve[i] != "o" and ve[i] != "u" and ve[i] != " "):
		ve = ve.replace(ve[i],"p")
print(ve)	