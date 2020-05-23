#from mach import* || round || .upper()

x = int(input("Quantidade de votos para Ambrosio Rutra: "))
y = int(input("Quantidade de votos para Demelza Olecram: "))
# q1 + q2 = 100%

total = x + y

p1 = (x * 100) / total
p2 = (y * 100) / total

if( p1 > p2 ):
	print("Ambrosio Rutra")
	print(round(p1, 2))
else:
	print("Demelza Olecram")
	print(round(p2, 2))