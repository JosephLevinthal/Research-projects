cabeca = input("cabeca: ")
d1 = int(input("dado 1: "))
d2 = int(input("dado 2: "))
if not(1<=d1<=10) or not(1<=d2<=10):
	print("Entrada invalida")
elif (cabeca.upper()== "AAMEUL"):
	dt = d1 + d2 + 8
	print(dt)
elif (cabeca.upper()== "HETHRADIAH"):
	dt = 2*(d1 + d2)
	print(dt)
elif (cabeca.upper()== "RAKSHASA"):
	dt = d1 + d2 + 10
	print(dt)