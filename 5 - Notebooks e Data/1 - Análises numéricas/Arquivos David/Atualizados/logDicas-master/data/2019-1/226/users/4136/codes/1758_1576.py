from numpy import*
e = array(eval(input("vetor e: "))) 
b = array(eval(input("vetor b: ")))
i = 0
somae = 0
somab = 0
while i < size(e):
	if(e[i] == 11 and b[i] == 33) or (e[i] == 22 and b[i] == 11) or (e[i] == 33 and b[i] == 22):
		somae = somae + 1
		i = i + 1
	elif(b[i] == 11 and e[i] == 33) or (b[i] == 22 and e[i] == 11) or (b[i] == 33 and e[i] == 22):
		somab = somab + 1
		i = i + 1
	else:
		i = i + 1
print(i)
if(somae>somab):
		print("EUSAPIA")
elif(somab>somae):
		print("BARSANULFO")
else:
		print("EMPATE")





