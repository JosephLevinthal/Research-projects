house = input("nome da casa: ")

if (( house != "lobo") and ( house != "leao") and ( house != "veado" ) and ( house != "dragao" ) and ( house != "rosa" ) and ( house != "sol" ) and ( house != "lula" ) and ( house != "esfolado" ) and ( house != "turta" )):
	print("Entrada:",house)
	print("Brasao invalido")
elif ( house == "lobo" ):
	print("Entrada:",house)
	print("Casa:","Stark")
elif ( house == "leao" ):
	print("Entrada:",house)
	print("Casa:","Lannister")
elif ( house == "veado" ):
	print("Entrada:",house)
	print("Casa:","Baratheon")
elif ( house == "dragao" ):
	print("Entrada:",house)
	print("Casa:","Targaryen")
elif ( house == "rosa" ):
	print("Entrada:",house)
	print("Casa:","Tyrell")
elif ( house == "sol" ):
	print("Entrada:",house)
	print("Casa:","Martell")	
elif ( house == "lula" ):
	print("Entrada:",house)
	print("Casa:","Greyjoy")
elif ( house == "esfolado" ):
	print("Entrada:",house)
	print("Casa:","Bolton")
elif ( house == "turta" ):
	print("Entrada:",house)
	print("Casa:","Tully")