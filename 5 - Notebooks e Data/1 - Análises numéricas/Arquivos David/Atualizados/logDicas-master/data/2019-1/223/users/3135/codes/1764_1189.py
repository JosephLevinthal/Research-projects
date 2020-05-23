frase = input("Escreva uma frase:")
frasenova=frase.replace(" ","")
print(frasenova.upper())


normal = frasenova[0:]
inverso = frasenova[::-1]

if(normal==inverso):
	s=1
else:
	s=0
print(s)