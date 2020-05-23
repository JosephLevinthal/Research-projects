m = int(input("Quant de moedas: "))
dm = int(input("Despesas mensal: "))
mo= float(input("Moedas de ouro : "))
r = float(input("Moedas roubadas: "))

meses = 1
x = 0
y = 0

while((mo + m) >= r):
	x = (m * mo) / 100
	r = r + x
	y = (dm * r) / 100
	mo = mo + y 
	meses = meses + 1
print(meses)
	
	