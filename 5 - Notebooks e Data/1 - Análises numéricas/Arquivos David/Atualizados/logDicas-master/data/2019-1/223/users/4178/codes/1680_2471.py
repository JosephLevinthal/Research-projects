a = int(input("Idade: "))
b = float(input("IMC: "))

if (a <= 0) or (a > 130) or (b <= 0):
	msg = "Dados invalidos"

elif (a < 45) and (b < 22): 
	msg = "Baixo"

elif	(a >= 45) and (b < 22):
	msg = "Medio"

elif (a < 45) and (b >= 22):
	msg = "Medio"

elif (a >= 45) and (b >= 22):
	msg = "Alto"

print("Entrada:", a , "anos e IMC",b)
print("Risco:",msg)