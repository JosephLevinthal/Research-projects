valor = float(input("Qual o seu valor disponivel?"))
tickets = int(input("Quantos tickets deseja comprar?"))
vt = float(input("Quanto custa um ticket?"))
passes = int(input("Quantos passes de onibus deseja comprar?"))
vp = float(input("Valor dos passes"))

if(valor>= tickets*vt + passes*vp):
  print("SUFICIENTE")
else:
	print("INSUFICIENTE")