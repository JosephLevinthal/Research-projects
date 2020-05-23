v = float(input("consumo em kWh: "))
t = input("tipo de instalacao ")
if(t != "C") or (t != "R") or (t != "I") or (v <= 0):
	print("Dados invalidos")
elif(t == C) and (v <= 500):
	print(v*0,44)
elif(t == C) and (v>500):
	print(v*0,66)
elif(t == C) and (v<=1000):
	print(v*0,55)
elif(t == C) and (v>1000):
	print(v*0,60)