a = int(input("numero de habitantes: "))
b = int(input("numero de habitantes: "))
pa = float(input("percentual: "))
pb = float(input("percentual: "))
a1 = a
b1 = b
tempo = 0
while (a1 <= b1):
	tempo = tempo + 1
	a1 = a + (pa/100 * a)
	b1 = b + (pb/100 * b)
print(tempo)