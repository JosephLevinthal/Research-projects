c1 = int(input("Numeros de habitantes: "))
c2 = int(input("Numeros de habitantes: "))
p1 = float(input("Qual a porcentagem? "))
p2 = float(input("Qual a porcentagem? "))

anos = 0
hab1 = c1
hab2 = c2

while ( hab1 < hab2 ):
	
	anos = anos + 1
	hab1 = hab1 + (hab1 * p1/100)
	hab2 = hab2 + (hab2 * p2/100)
	
print( anos )