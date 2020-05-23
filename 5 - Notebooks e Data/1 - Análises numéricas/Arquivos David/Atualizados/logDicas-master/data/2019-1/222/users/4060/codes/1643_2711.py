valor=float(input("valor disponivel: "))
q_tickets=int(input("quantidade de tickets: "))
v_tickets=float(input("valor dos tickets: "))
q_passes=int(input("passes de onibus: "))
v_passes=float(input("valor dos passes: "))
totaltickets=q_tickets*v_tickets
totalpasses=q_passes*v_passes
total=totaltickets+totalpasses
if(valor>=total):
	men="suficiente"
else:
	men="insuficiente"
print(men.upper())	
	

