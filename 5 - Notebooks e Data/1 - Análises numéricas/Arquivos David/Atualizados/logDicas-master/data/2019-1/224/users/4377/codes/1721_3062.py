po=int(input("po"))
ar=input("nome")
ft=int(input("ft"))
ar=ar.upper()
if((ft>=1 and ft<=10) and (ar== "ESPADA" or ar=="MACHADO" or ar=="MARRETA")):
	if(ar=="ESPADA" and po>=100 ):
		ft=ft*10
		print(ft)
	if(ar=="MACHADO" and po>=30):
		ft=ft+3
		print(ft)
	if(ar=="MARRETA" and po>=50):
		ft=ft+5
		print(ft)
	if(ar=="ESPADA" and po<100):
		print("PO insuficiente")
	if(ar=="MACHADO" and po<30):
		print("PO insuficiente")
	if(ar=="MARRETA" and po<50):
		print("PO insuficiente")		
else:
	print("Entrada invalida")
	
	


