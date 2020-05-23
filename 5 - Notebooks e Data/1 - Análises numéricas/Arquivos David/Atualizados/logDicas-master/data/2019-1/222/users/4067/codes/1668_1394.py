horas = float(input("horas trabalhadas: "))
if horas <= 20:
	mensagem = round(horas * 50,2) 
else:
	mensagem = round((20*50) + (horas - 20)*70,2)
print (mensagem)