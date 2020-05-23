qi = int(input("quantidade inicial:"))
c = int(input("crescimento da parada:"))
lim = 8000
t = 0
while (0<qi<lim):
	v = int(input("peixes tirados: "))
	qi = qi - v + c*qi/100
	t = t+1
if (qi <= 0):
	print("ZERO")
elif (qi>=lim):
	print("MAXIMO")
print(t)