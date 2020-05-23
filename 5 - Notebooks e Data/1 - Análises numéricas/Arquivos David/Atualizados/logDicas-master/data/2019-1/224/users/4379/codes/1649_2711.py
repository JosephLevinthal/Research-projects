val=float(input("valor disponivel:"))
qtdru=int(input("quantidade de tickets:"))
valtic=float(input("valor do ticket:"))
qtdbus=int(input("quantidade de passes:"))
valbus=float(input("valor dos passes:"))
valor= (qtdru * valtic) + (qtdbus * valbus)
if val > valor:
     print("SUFICIENTE")
else:
	  print("INSUFICIENTE")