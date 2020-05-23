from numpy import*

sa = input("string:") 
letra = ''
for i in sa:
	if(i != 'a' and i != 'A'):
		letra = letra + i
print(letra)