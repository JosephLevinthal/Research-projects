qac = float(input("Digite a quantidade de acai em gramas: "))
qs = int(input("Digite a quantidade de salgados: "))
vd = float(input("Digite o valor em dinheiro: "))
ps = 3.0 #preço do salgado
aKG = 24.0  #preço do kg do açaí
t = vd - (((24.0*qac) / 1000)) + (qs*3.0)
if(t > 0):
	m = "Sim"
	print(round(t, 2))
	print(m)
else:
	m = "Nao"
	print(m)
	
