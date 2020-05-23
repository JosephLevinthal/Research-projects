tempo = int(input(""))

if (tempo <= 200):
	custo = 5000 + 100 * tempo
	print(round(custo,2))
else:
	custo = 8000 + 100 * 200 + 90 * (tempo - 200)
	print(float(round(custo,2)))