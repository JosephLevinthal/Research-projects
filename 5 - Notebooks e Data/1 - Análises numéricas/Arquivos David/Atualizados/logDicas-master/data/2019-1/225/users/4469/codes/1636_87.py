aleatorio1 = int(input())
aleatorio2 = int(input())
aleatorio3 = int(input())

if(aleatorio1 <= aleatorio3):
	if(aleatorio1 <= aleatorio2):
		print(aleatorio1)
	else:
		print(aleatorio2)
else:
	if(aleatorio1 <= aleatorio2):
		if(aleatorio1 <= aleatorio3):
			print(aleatorio1)
		else:
			print(aleatorio3)
	else:
		if(aleatorio2 <= aleatorio3):
			print(aleatorio2)
		else:
			print(aleatorio3)