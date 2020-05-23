from numpy import*
v1 = array(eval(input("n: ")))
v2 = array(eval(input("n: ")))
pedra = 11
papel = 22
tesoura = 33
c = 0
ve = 0
vb = 0

while(c<size(v1)):
	if(v1[c] == pedra and v2[c] == papel):
		vb = vb + 1
	elif(v1[c] == pedra and v2[c] == tesoura):
		ve = ve + 1
	elif(v1[c] == papel and v2[c] == tesoura):
		vb = vb + 1
	elif(v1[c] == papel and v2[c] == pedra):
		ve = ve + 1
	elif(v1[c] == tesoura and v2[c] == papel):
		ve = ve + 1
	elif(v1[c] == tesoura and v2[c] == pedra):
		vb = vb + 1		
	c = c + 1
print(size(v1))
if(ve>vb):
	print("EUSAPIA")
elif(vb>ve):
	print("BARSANULFO")
else:
	print("EMPATE")