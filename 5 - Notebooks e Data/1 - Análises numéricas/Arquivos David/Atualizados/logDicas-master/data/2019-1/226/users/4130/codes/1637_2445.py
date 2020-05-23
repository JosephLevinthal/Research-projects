temp = input("A escala da temperatura (C ou F): ")
valtemp = float(input("A temperatura: "))

c = (5 / 9) * (valtemp - 32)
f = (valtemp * (9 / 5)) + 32

if (temp.upper() == "F"):
	mensagem = c
if (temp.upper() == "C"):
	mensagem = f
	
print(mensagem)