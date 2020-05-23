horas = int(input("horas semanais: "))
ganho = float(20*50 + (horas - 20)*70)
if(horas<=20):
	mensagem = float(horas*50)
else:
	mensagem = (ganho)
print(mensagem)