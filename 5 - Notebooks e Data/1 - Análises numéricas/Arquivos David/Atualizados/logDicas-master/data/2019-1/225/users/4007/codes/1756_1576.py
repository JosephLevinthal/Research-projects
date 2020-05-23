from numpy import*
e = array(eval(input("jogadas de eusapia: ")))
b = array(eval(input("jogadas de barsan: ")))
pedra = 11
papel = 22
tesoura = 33
c = 0
ve = 0
vb = 0
while (c < size(e)):
	if (e[c] == pedra and b[c] == papel):
		vb = vb + 1
	elif (e[c] == tesoura and b[c] == pedra):
		vb = vb + 1
	elif (e[c] == papel and b[c] == tesoura):
		vb = vb + 1
	elif (e[c] == papel and b[c] == pedra ):
		ve = ve + 1
	elif (e[c] == pedra and b[c] == tesoura):
		ve = ve + 1
	elif (e[c] == tesoura and b[c] == papel):
		ve = ve + 1
	c = c + 1
print(size(e))
if (ve > vb):
	print("EUSAPIA")
elif (vb > ve):
	print("BARSANULFO")
else:
	print("EMPATE")
	
	