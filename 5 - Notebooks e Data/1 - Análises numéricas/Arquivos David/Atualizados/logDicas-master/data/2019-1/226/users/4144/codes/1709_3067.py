atk= input("tipo de ataque, cauda ou espada?: ").upper()
a= int(input("valor sorteado do dado: "))
b= int(input("valor sorteado do dado: "))
c= int(input("valor sorteado do dado: "))
d= int(input("valor sorteado do dado: "))
if((a>=1) and (a<=6) and (b>=1) and (b<=6) and (c>=1) and (c<=6) and (d>=1) and (d<=6) and (atk=="CAUDA") or (atk=="ESPADA")):
	if(atk=="CAUDA"):
		print((a+b+c)*d)
	elif(atk=="ESPADA"):
		print(a+6+b+6+c+6+d+6)
else:
	print("Entrada invalida")