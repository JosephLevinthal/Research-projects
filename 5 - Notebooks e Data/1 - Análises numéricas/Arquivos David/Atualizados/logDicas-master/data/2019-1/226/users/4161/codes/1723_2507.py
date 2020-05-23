qi = int(input("quantidade incial de peixes: "))
c = int(input("crescimento: "))
lim = 8000
t = 0
while (0 < qi < lim):
	v = int(input("peixes tirados pra venda: "))
	qi = qi - v + c*qi/100
	t = t + 1
if (qi<= 0):
	print("ZERO")
elif (qi>=lim):
	print("MAXIMO")
print(t)