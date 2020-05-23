rs= float(input("Digite a: ")) 
nru = int(input("Digite : ")) 
vru = float(input("Digite a: ")) 
nbus = int(input("Digite : ")) 
vbus = float(input("Digite : ")) 

calc= (nru*vru) + (nbus*vbus)
if(calc<=rs):
	
	print("SUFICIENTE")
else:
	print("INSUFICIENTE")
