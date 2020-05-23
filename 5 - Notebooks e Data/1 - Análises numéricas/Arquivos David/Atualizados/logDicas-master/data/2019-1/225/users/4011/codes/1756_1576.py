from numpy import*

v = array(eval(input("Jogadas de eu: ")))
u = array(eval(input("Jogadas de ba: ")))

i = 0
ve = 0
vb = 0

pedra = 11
papel = 22
tesoura = 33

while( i < size(v)):
	if(v[i] == pedra and u[i] == tesoura):
		ve = ve + 1
	elif(v[i] == papel and u[i] == pedra):
		ve = ve + 1
	elif(v[i] == tesoura and u[i] == papel):
		ve = ve + 1
	elif(u[i] == pedra and v[i] == tesoura):
		vb = vb + 1
	elif(u[i] == papel and v[i] == pedra):
		vb = vb + 1
	elif(u[i] == tesoura and v[i] == papel):
		vb = vb + 1
	i = i + 1
	
print(size(v))
if(ve > vb):
	print("EUSAPIA")
elif(ve < vb):
	print("BARSANULFO")
else:
	print("EMPATE")
