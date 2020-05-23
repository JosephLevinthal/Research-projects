from numpy import*
frase = input("insira sua frase: ")
sfrase = frase.replace(" ", "")
print(sfrase.upper())
invert = (frase[::-1])
if(invert==frase):
	print("1")
else:
	print("0")
