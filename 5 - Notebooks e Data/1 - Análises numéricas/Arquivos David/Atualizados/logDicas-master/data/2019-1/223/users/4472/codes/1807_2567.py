base = int(input("Informe o tamanho da base: "))

#parte de cima
for j in range(0,base):
	
	for i in range(0,base - j):
		print("*",end="")
	print("\n",end="")
	
#parte debaixo	
for j in range(0,base):
	for i in range(0, j+1):
		print("*",end="")
	print("\n",end="")