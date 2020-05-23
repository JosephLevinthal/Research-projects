valor = float(input("reais: "))
ru = int(input("quant.: "))
valor_ru = float(input("vr: "))
bus_passes = int(input("bus: "))
valor_passes = float(input("vp: "))

if(valor > 300):
	mensagem = "SUFICIENTE"
else:
	mensagem = "INSUFICIENTE"
	
print(mensagem)