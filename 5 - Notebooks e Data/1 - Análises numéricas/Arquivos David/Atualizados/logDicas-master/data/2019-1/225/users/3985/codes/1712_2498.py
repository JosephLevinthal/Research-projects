na= int(input("Numero de habitantes de uma cidade A:"))
nb= int(input("Numero de habitantes de uma cidade B:"))
pa= float(input("Percentual de crescimento populacional da cidade A:"))
pb= float(input("Percentual de crescimento populacional da cidade B:"))

t=0
while (na < nb):
	k= (na*pa)/100
	na= na+k
	g= (nb*pb)/100
	nb= nb+g
	t= t+1
print(t)
		