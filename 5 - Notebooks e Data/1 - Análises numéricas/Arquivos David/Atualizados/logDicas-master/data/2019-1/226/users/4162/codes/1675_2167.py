d= input("insira o nome da cidade de destino: ").lower()
p= input("insira se o percurso e somente de ida ou ida-e-volta: ").lower()

if (d=="belem")and(p=="ida"):
	print("350.0")
elif (d=="belem")and(p=="ida-e-volta"):
	print("650.0")
elif (d=="borba")and(p=="ida"):
	print("80.0")
elif (d=="borba")and(p=="ida-e-volta"):
	print("152.0")
elif (d=="coari")and(p=="ida"):
	print("106.0")
elif (d=="coari")and(p=="ida-e-volta"):
	print("199.0")
elif (d=="humaita")and(p=="ida"):
	print("200.0")
elif (d=="humaita")and(p=="ida-e-volta"):
	print("390.0")
elif (d=="manicore")and(p=="ida"):
	print("150.0")
elif (d=="manicore")and(p=="ida-e-volta"):
	print("280.0")
elif (d=="maues")and(p=="ida"):
	print("100.0")
elif (d=="maues")and(p=="ida-e-volta"):
	print("190.0")
else:
	print("Destino inexistente")