tempo = int(input("Tempo: "))

i = (1042000/1500)**(1/tempo) - 1

if (i <= 0.01):
	print(round(i,5))
	print("Real")
	
else:
	print(round(i,5))
	print("Irreal")