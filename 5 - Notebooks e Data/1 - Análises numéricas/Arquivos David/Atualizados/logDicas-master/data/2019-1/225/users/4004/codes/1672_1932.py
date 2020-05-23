So1 = float(input("Distancia entre os olhos, da Imagem 1: "))
Sn1 = float(input("Distancia entre o nariz e o queixo, da Imagem 1: "))
So2 = float(input("Distancia entre os olhos, da Imagem 2: "))
Sn2 = float(input("Distancia entre o nariz e o queixo, da Imagem 2: "))
So3 = float(input("Distancia entre os olhos, da Imagem 3: "))
Sn3 - float(input("Distancia entre o nariz e o queixo, da Imagem 3: "))

S1 = So1 / Sn1
S2 = So2 / Sn2
S3 = So3 / Sn3

if (abs(S1 - S2) < abs(S2 - S3 )) and (abs(S1 - S2) < abs(S1 - S3)):
	