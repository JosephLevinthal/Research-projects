from numpy import*
preco= array(eval(input("vetor custo dos produtos: ")))
pagar=0
pro=0
desconto= 0
while (pro< size(preco)):
	if (preco[pro] <= 80.0):
		pagar= pagar + preco[pro]
		pro= pro + 1
	elif (preco[pro] > 80.0):
		pagar = pagar + preco[pro] - 5
		pro = pro + 1
print(round(pagar, 2))
