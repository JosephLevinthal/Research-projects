from numpy import*

l = input("Escreve tua frase ae:").lower()

I = 0

while(I < size(l)):
	
	if(l[I]!= "a" or  l[I]!= "e" or l[I]!= "i" or l[I]!= "o" or l[I]!= "u"):
		l = l.replace(l[I],"p")
	I = I + 1
print(l)