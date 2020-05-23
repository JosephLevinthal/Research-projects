P1= float(input("Insira a sua altura:"))
P2= float(input("Insira a altura do acompanhante:"))
mi= 1.37
if (max(P1,P2) >= 1.37):
	msg= "Sim"
else:
	msg= "Nao"
	
print(msg)
print(max(P1,P2))