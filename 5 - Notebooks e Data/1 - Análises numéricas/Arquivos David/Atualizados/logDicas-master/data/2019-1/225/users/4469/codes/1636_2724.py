aleatorio1 = int(input())
aleatorio2 = int(input())
aleatorio3 = int(input())

if(aleatorio1 <= aleatorio3):
	if(aleatorio1 <= aleatorio2):
		print(aleatorio2)
	else:
		print(aleatorio1)
else:
	if(aleatorio1 <= aleatorio2):
		if(aleatorio1 <= aleatorio3):
			print(aleatorio3)
		else:
			print(aleatorio1)
	else:
		if(aleatorio2 <= aleatorio3):
			print(aleatorio3)
		else:
			print(aleatorio2)