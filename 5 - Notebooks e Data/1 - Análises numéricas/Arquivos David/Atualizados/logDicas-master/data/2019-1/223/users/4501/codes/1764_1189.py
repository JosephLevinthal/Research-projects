frase = input("Digite uma palavra ou frase: ")

frase = frase.upper()
new = frase.replace("","")
inv = ""
i = -1

while(i >= -len(new)):
	inv = inv+new[i]
	i = i-1
print(new)
if(new == inv):
	print(1)
else:
	print(0)