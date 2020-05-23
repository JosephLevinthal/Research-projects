from numpy import*
v0 = array(eval(input("n: ")))
v1 = array(eval(input("n1: ")))

pedra = 11
papel = 22
tesoura = 33

c = 0
ve = 0
vb = 0

while(c < size(v0)):
	if(v0[c] == pedra and v1[c] == tesoura):
		ve = ve + 1
	elif(v0[c] == pedra and v1[c] == papel):
		vb = vb + 1
	elif(v0[c] == tesoura and v1[c] == papel):
		ve = ve + 1
	elif(v0[c] == tesoura  and v1[c] == pedra):
		vb = vb + 1
	elif(v0[c] == papel and v1[c] == pedra):
		ve = ve +1
	elif(v0[c] == papel and v1[c] == tesoura):
		vb = vb + 1
	c = c + 1

print(size(v0))
if(ve > vb):
		print("EUSAPIA")
elif(vb > ve):
		print("BARSANULFO")
else:
		print("EMPATE")
