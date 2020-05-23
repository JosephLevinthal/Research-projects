from numpy import*
t = input("tipo de espada: ").upper()
n = array(eval(input("nivel/dano: ")))

i = 0
s = 0
while (i < size(n)):
	if (t[i] == "CENOURA"):
		a = 2
		b = 0
		c = 0
		d = 0
		e = 0
	elif(t[i] == "DWARVEN"):
		b = 8
		a = 0
		c = 0
		e = 0
		
	elif (t[i] == "FERRO"):
		c = 4
		a = 0
		b = 0
		d = 0 
		e = 0

	elif (t[i] == "ELVEN"):
		a = 0
		b = 0
		c = 0
		d = 11
		e = 0
	elif(t[i] == "DAEDRIC"):
		a = 0 
		b = 0
		c = 0
		d = 0
		e = 14
	i = i + 1
dano = t[i] * n
print(dano)
		

