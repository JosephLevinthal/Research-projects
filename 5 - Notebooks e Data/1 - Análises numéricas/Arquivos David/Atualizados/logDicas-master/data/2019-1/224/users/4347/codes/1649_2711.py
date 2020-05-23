valorD = float(input("saldo dispunivel,sinhor:"))
Qtikets = int(input("quantos tiket`s deseja, sinhor:"))
Vtikets = float(input("quanto custa cada tiket, sinhor"))
Qpass = int(input("quantos passes deseja, sinhor:"))
Vpass = float(input("valor dos passes , sinhor:"))
if valorD < ((Qtikets*Vtikets)+(Qpass*Vpass)):
	print("INSUFICIENTE")
else:
	print("SUFICIENTE")