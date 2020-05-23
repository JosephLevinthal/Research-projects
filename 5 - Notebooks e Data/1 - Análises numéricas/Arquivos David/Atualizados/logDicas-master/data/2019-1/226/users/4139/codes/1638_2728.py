d = float(input("percurso em km:"))
t = input("tipo do carro A ou B:")

if(t == "A"):
	x = d/8
else:
	x = d/12
print(round(x,2))