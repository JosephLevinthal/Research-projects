from numpy import*

f = input("Sua frase:").lower()

i = 0
v = 0 #vogais
d = ""
while(i != len(f)):
	if(f[i] == "a" or "e" or "i" or "o" or "u" ):
		v = v+1
	i = i+1
print()