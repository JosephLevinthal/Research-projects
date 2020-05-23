q1 = int(input("copias do virus:"))
q2 = int(input("leucocitos:"))
p1 = int(input("percentual do virus:")) 
p2 = int(input("percentual de leucocitos:")) 

cont = 0

while(q2 / q1 < 2):
	q1 = q1 + (q1 * p1/100)
	q2 = q2 + (q2 * p2/100)
	cont = cont + 1
print(cont)