from numpy import*

falta = array(eval(input("digite as faltas: ")))
f = size(falta)
a = zeros(6, dtype=int)

a1 = 0
a2 = 0
a3 = 0
a4 = 0
a5 = 0
a6 = 0

for i in range(size(falta)):
		if	(falta[i] == 2):
			a1 = a1 + 1
		elif(falta[i] == 3):
			a2 = a2 + 1
		elif(falta[i] == 4):
			a3 = a3 + 1
		elif(falta[i] == 5):
			a4 = a4 + 1
		elif(falta[i] == 6):
			a5 = a5 + 1
		elif(falta[i] == 7):
			a6 = a6 + 1
				
		a[0] = a1
		a[1] = a2
		a[2] = a3
		a[3] = a4
		a[4] = a5
		a[5] = a6
m = zeros(6)
for z in range(6):
	po = round(((a[z]/sum(a))*100), 1)
	m[z] = po
	
	

print(m)
	