frase = input("digite um frase:")
frase_2 = ""
for ch in range(len(frase)):
	if( (frase[ch] != "a") and (frase[ch] != "e") and (frase[ch] != "i") and (frase[ch] != "o") and (frase[ch] != "u")):
		frase_2 = frase_2 + frase[ch]
print(frase_2)