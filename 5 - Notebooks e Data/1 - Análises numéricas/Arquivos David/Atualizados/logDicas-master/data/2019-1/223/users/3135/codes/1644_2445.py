E=input("Escala da temperatura:(F/C)")
T=float(input("Valor da temperatura:"))

if (E.upper() ==  "F"):
	t= 5/9*(T-32)	
else:
	t= (T*9/5)+32

print(round(t,2))