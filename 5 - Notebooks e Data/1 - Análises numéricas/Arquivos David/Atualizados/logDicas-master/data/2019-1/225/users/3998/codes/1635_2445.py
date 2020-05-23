opcao = input("temperatuara em (F/ C)")
if (opcao=="C"):
	c = (int(input("temperatura: ")))
	f = (1.8*c) + 32
	print(round(f,2))
else:
	f=(int(input("temperatura: ")))
	c = 5/9*(f - 32)
	print(round(c,2))

