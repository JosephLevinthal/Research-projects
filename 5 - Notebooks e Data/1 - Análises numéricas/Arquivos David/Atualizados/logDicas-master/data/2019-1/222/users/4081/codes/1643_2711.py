val=float(input("disponivel:"))
ru=int(input("ticketsdoru:"))
tic=float(input("valortickets:"))
bus=int(input("quantidadepassesonibus:"))
pas=float(input("valorpasses:"))
soma=(ru*tic)+(bus*pas)
if(soma<=val): 
	print("suficiente" .upper())
else:	
	print("insuficiente" .upper())
	