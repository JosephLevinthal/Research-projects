a= float(input("Insira o numero de habitantes da cidade A:"))
b= float(input("Insira o numero de habitantes da cidade B:"))
na= float(input("Percentual do crescimento da cidade A:"))
nb= float(input("Percentual do crescimento da cidade B:"))

pa= na/100
pb= nb/100

ha= a
hb= b
t = 0

while (ha<hb):
	acresA= ha*pa
	acresB= hb*pb
	ha= acresA+ ha
	hb= acresB+hb
	t=t+1
print(t)
	
	