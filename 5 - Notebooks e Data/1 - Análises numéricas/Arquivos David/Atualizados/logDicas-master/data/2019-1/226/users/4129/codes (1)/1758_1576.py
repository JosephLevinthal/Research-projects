from numpy import*

v = array(eval(input("Vetor 1: "))) #Eusapia
u = array(eval(input("Vetor 2: ")))  #Basanulfo

p = 0
a = 0
Bars = 0
Eusa = 0
x = 0
i = 0
while ( i < size(v)):
	if (v[p] == 11 and u[p] == 22 ):
		Bars = Bars + 1
	elif(v[p] == 22 and u[p] == 33):
		Bars = Bars + 1
	elif(v[p] == 33 and u[p] == 11):
		Bars = Bars + 1
	elif (v[p] == u [p]):
		x = x + 1
	else:
		Eusa = Eusa + 1
	a = a + 1
	i = i + 1
	p = p + 1

print(a)	
	
if ( Bars > Eusa):
	print("BARSANULFO")
elif(Eusa > Bars):
	print('EUSAPIA')
else:
	print("EMPATE")