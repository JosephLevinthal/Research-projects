tempo = int(input("Tempo de voo: "))
if tempo <= 200 :
	v = (100 * tempo) + 5000
	print(v)
else :
	a = tempo - 200
	v = 8000 + ((100 * 200) + (90*a))
	print(v)