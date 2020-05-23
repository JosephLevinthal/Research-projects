a = int(input("Digite a quantidade de votos para Ambrosio: "))
d = int(input("Digite a quantidade de votos para Demelza: "))
x = a + d

if (a > d):
	print("Ambrosio Rutra")
	r = (a / x) * 100
	print(round(r,2))
else: 
	print("Demelza Olecram")
	r = (d / x) * 100
	print(round(r,2))