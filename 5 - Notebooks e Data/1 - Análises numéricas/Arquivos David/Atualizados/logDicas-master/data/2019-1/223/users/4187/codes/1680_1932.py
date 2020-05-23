do1 = float(input("distancia entre  os olhos, da imagem 1:"))
dnq1 = float(input("distancia entre o nariz e o queixo, da imagem 1:"))
do2 = float(input("distancia entre  os olhos, da imagem 2:"))
dnq2 = float(input("distancia entre o nariz e o queixo, da imagem 2:"))
do3 = float(input("distancia entre  os olhos, da imagem 3:"))
dnq3 = float(input("distancia entre o nariz e o queixo, da imagem 3:"))

# "face" é Razao entre duas medidas: diastanca entre os olhos e  a distancia entre o nariz e o queixo
face1 = do1/dnq1
face2 = do2/dnq2
face3 = do3/dnq3

#comparacao de difenca entre as faces
comp12 = abs(face1 - face2)
comp13 = abs(face1 - face3)
comp23 = abs(face2 - face3)

menorDiferenca = min(comp12,comp13,comp23)
if(menorDiferenca == comp12):
	print("1 e 2")
elif(menorDiferenca == comp13):
	print("1 e 3")
elif(menorDiferenca == comp23):
	print("2 e 3")







