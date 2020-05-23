per=float(input("percurso em km: "))
car=input("tipo de carro (A/B): ")

if(car.upper() == "A"):
	cons=per/8
else:
	cons=per/12

print(round(cons,2))