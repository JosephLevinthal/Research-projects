metade = int(input("metade dos asteriscos na primeira linha")) * 2

ast = "*"
linha_1 = ast * metade

QA2 = (len(linha_1)- 2)//2

oo = "oo"
mult = 1
print(linha_1)

ll = (ast * QA2 ) + (oo * mult ) + (ast * QA2 )

for ch in range(0,len(linha_1)):
	if (QA2 <= len(ll)-1 and (mult <= (len(linha_1) - 2)/2)):
		ll = (ast * QA2 ) + (oo * mult ) + (ast * QA2 ) 
		print(ll)
		QA2 = QA2 - 1
		mult = mult + 1